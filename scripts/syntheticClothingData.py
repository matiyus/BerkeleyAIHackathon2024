import pandas as pd
import numpy as np


# Define possible values for each feature
clothing_types = ['Jacket', 'Shirt', 'Leggings', 'Shorts', 'Tank Top']
sizes = ['XS', 'S', 'M', 'L', 'XL', 'XXL']
materials = ['Cotton', 'Polyester', 'Wool', 'Linen', 'Silk', 'Spandex', 'Nylon']
seasons = ['Winter', 'Spring', 'Summer', 'Fall']
colors = ['Black', 'Red', 'Blue', 'Green', 'White']
activity_types = ['Running', 'Yoga', 'Weightlifting', 'Cycling']
compression_levels = ['Low', 'Medium', 'High']
moisture_wicking = ['Yes', 'No']
breathability_levels = ['Low', 'Medium', 'High']
elasticity_levels = ['Low', 'Medium', 'High']
uv_protection = ['Yes', 'No']
reflective_elements = ['Yes', 'No']
pockets_options = [0, 1, 2, 3]
waistband_types = ['Elastic', 'Drawstring']
fit_styles = ['Slim', 'Regular', 'Relaxed']
brand_name = ['Nike','Adidas']

# Generate random data for clothing items
num_clothing_items = 1000
clothing_data = {

    'clothing_id': np.arange(1, num_clothing_items + 1),
    'clothing_type': np.random.choice(clothing_types, num_clothing_items),
    'size': np.random.choice(sizes, num_clothing_items),
    'material': np.random.choice(materials, num_clothing_items),
    'season': np.random.choice(seasons, num_clothing_items),
    'color': np.random.choice(colors, num_clothing_items),
    'waist': np.random.randint(24, 40, num_clothing_items),
    'chest': np.random.randint(30, 50, num_clothing_items),
    'hip': np.random.randint(30, 50, num_clothing_items),
    'length': np.random.randint(20, 40, num_clothing_items),
    'activity_type': np.random.choice(activity_types, num_clothing_items),
    'compression_level': np.random.choice(compression_levels, num_clothing_items),
    'moisture_wicking': np.random.choice(moisture_wicking, num_clothing_items),
    'breathability': np.random.choice(breathability_levels, num_clothing_items),
    'elasticity': np.random.choice(elasticity_levels, num_clothing_items),
    'uv_protection': np.random.choice(uv_protection, num_clothing_items),
    'reflective_elements': np.random.choice(reflective_elements, num_clothing_items),
    'pockets': np.random.choice(pockets_options, num_clothing_items),
    'inseam_length': np.random.randint(0, 10, num_clothing_items),  # Example inseam lengths
    'waistband_type': np.random.choice(waistband_types, num_clothing_items),
    'fit_style': np.random.choice(fit_styles, num_clothing_items),
    'brand_name': np.random.choice(brand_name, num_clothing_items)
}

# Adjusting dimensions to be 0 where not applicable (e.g., chest for leggings)
for i in range(num_clothing_items):
    if clothing_data['clothing_type'][i] in ['Leggings', 'Shorts']:
        clothing_data['chest'][i] = 0
    if clothing_data['clothing_type'][i] in ['Shirt', 'Tank Top']:
        clothing_data['hip'][i] = 0

# Convert to DataFrame
clothing_df = pd.DataFrame(clothing_data)

# Save to CSV
clothing_df.to_csv('synthetic_clothing_data.csv', index=False)

# Save to JSON
clothing_df.to_json('synthetic_clothing_data.json', orient='records', lines=True)
