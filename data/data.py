import pandas as pd
import numpy as np

# Define the function to check if the clothing fits
def check_fit(user_chest, user_length, cloth_chest, cloth_length):
    return int(
        user_chest <= cloth_chest and 
        user_length <= cloth_length
    )

# Load the clothing measurements into a DataFrame
cloth_df = pd.DataFrame({
    'cloth_chest': [20, 22, 24, 26],
    'cloth_length': [27.5, 28.5, 29.5, 30.5]
})

# Generate realistic user measurements
def generate_user_measurements(num_samples):
    base_sizes = [
        {'chest': 19, 'length': 26},
        {'chest': 21, 'length': 27},
        {'chest': 23, 'length': 28},
        {'chest': 25, 'length': 29},
        {'chest': 27, 'length': 30},
    ]

    user_measurements = []
    for _ in range(num_samples):
        base_size = np.random.choice(base_sizes)
        if np.random.rand() > 0.5:
            # Create a fitting measurement
            user_measurement = {
                'user_chest': base_size['chest'] + np.random.randint(-1, 1),
                'user_length': base_size['length'] + np.random.uniform(-0.5, 0.5),
            }
        else:
            # Create a non-fitting measurement by making chest or length exceed limits
            user_measurement = {
                'user_chest': base_size['chest'] + np.random.randint(1, 4),
                'user_length': base_size['length'] + np.random.uniform(0.5, 3.0),
            }
        user_measurements.append(user_measurement)
    
    # Add boundary cases (edge cases)
    for base_size in base_sizes:
        # Just fitting
        user_measurements.append({'user_chest': base_size['chest'], 'user_length': base_size['length']})
        # Just not fitting
        user_measurements.append({'user_chest': base_size['chest'] + 1, 'user_length': base_size['length'] + 0.1})
        # Outliers
        user_measurements.append({'user_chest': base_size['chest'] + 5, 'user_length': base_size['length'] + 5})

    return pd.DataFrame(user_measurements)

# Generate 30 user measurements
num_samples = 100000
user_measurements_df = generate_user_measurements(num_samples)

# Initialize a list to store the results
results = []

# Iterate over each user's measurements
for index, user_row in user_measurements_df.iterrows():
    fits = 0
    matching_cloth = {'cloth_chest': None, 'cloth_length': None}
    for cloth_index, cloth_row in cloth_df.iterrows():
        if check_fit(
            user_row['user_chest'], 
            user_row['user_length'], 
            cloth_row['cloth_chest'], 
            cloth_row['cloth_length']
        ):
            fits = 1
            matching_cloth = cloth_row
            break
        else:
            matching_cloth = cloth_row
    results.append({
        'user_chest': user_row['user_chest'],
        'user_length': user_row['user_length'],
        'cloth_chest': matching_cloth['cloth_chest'],
        'cloth_length': matching_cloth['cloth_length'],
        'fits': fits
    })

# Convert results to DataFrame
results_df = pd.DataFrame(results)

# Save the results to a new CSV file
results_df.to_csv('fitting_results.csv', index=False)

print(results_df)
