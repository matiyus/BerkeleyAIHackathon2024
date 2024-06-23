from fastapi import FastAPI, Request, Form
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from pydantic import BaseModel
from typing import Optional
from script.train import OSMEModel
from numpy import array as nparray

# fastapi dev main.py to run

app = FastAPI()
app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")


class FormData(BaseModel):
    user_chest: Optional[float] = None
    user_length: Optional[float] = None
    cloth_chest: Optional[float] = None
    cloth_length: Optional[float] = None

    def is_empty(self) -> bool:
        return any(
            (value is None) for value in 
            [self.user_chest, self.user_length, self.cloth_chest, self.cloth_length]
        )

    def is_zero(self) -> bool:
        return any(
            (value == 0.0) for value in 
            [self.user_chest, self.user_length, self.cloth_chest, self.cloth_length]
        )
    
    def is_negative(self) -> bool:
        return any(
            (value < 0.0) for value in 
            [self.user_chest, self.user_length, self.cloth_chest, self.cloth_length]
        )

lightweight_model = OSMEModel()
lightweight_model.read_data()
lightweight_model.train_data()

@app.get("/", response_class=HTMLResponse)
async def initial_launch(request: Request):
    form_data = FormData()
    return templates.TemplateResponse("index.html", {"request": request,
                                                     "message": "Welcome! Please enter your measurements.",
                                                     "form_data": form_data})

@app.post("/", response_class=HTMLResponse)
async def handle_form(request: Request,
                      user_chest: Optional[float] = Form(None),
                      user_length: Optional[float] = Form(None),
                      cloth_chest: Optional[float] = Form(None),
                      cloth_length: Optional[float] = Form(None)):
    form_data = FormData(user_chest=user_chest, user_length=user_length, cloth_chest=cloth_chest, cloth_length=cloth_length)
    if form_data.is_empty():
        return_data = "Some of the fields are missing."
    elif form_data.is_zero():
        return_data = "Some fields must not be zero."
    elif form_data.is_negative():
        return_data = "Can't have negative values."
    else:
        predicted_bool = lightweight_model.predict(form_data.user_chest,
                                                form_data.user_length,
                                                form_data.cloth_chest,
                                                form_data.cloth_length)
        if predicted_bool:
            return_data = "It fits!"
        else:
            return_data = "It doesn't fit!"
    return templates.TemplateResponse("index.html", {"request": request,
                                                     "message": return_data,
                                                     "form_data": form_data})
