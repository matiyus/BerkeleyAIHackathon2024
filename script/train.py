import pandas as pd
import numpy as np
import time
from sklearn.model_selection import train_test_split
from sklearn.ensemble import ExtraTreesClassifier
import matplotlib.pyplot as plt
from sklearn import metrics

class OSMEModel:
    data: pd.DataFrame = None
    model_forest: ExtraTreesClassifier = ExtraTreesClassifier()

    def __init__(self) -> None:
        pass

    def read_data(self):
        filename = "./data/fitting_results.csv"
        names = ['user_chest','user_length','cloth_chest','cloth_length','fits']
        self.data = pd.read_csv(filename, names=names, delimiter=',')
    
    def train_data(self):
        input, output = self.data.iloc[:,:4], self.data.iloc[:,4]
        input_train, input_test, output_train, output_test = train_test_split(input, output, train_size=0.7, random_state=123)

        t1 = time.time()
        self.model_forest.fit(input_train, output_train)
        t2 = time.time()
        print(f"Training time: {(t2 - t1)}ms")
                
        output_prediction = self.model_forest.predict(input_test)
        accuracy = np.mean(output_test == output_prediction)
        print(f"Expected Accuracy: {accuracy*100}%")

        disp = metrics.ConfusionMatrixDisplay.from_predictions(output_test, output_prediction)
        disp.figure_.suptitle("Confusion Matrix")
        print(f"Confusion matrix:\n{disp.confusion_matrix}")

        plt.show()
    
    def predict(self, user_chest: float, user_length: float, cloth_chest: float, cloth_length: float) -> float:
        input_data = np.array([[user_chest, user_length, cloth_chest, cloth_length]])
        prediction = self.model_forest.predict(input_data)
        print(prediction)
        return float(prediction[0])
