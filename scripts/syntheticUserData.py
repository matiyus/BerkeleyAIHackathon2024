import pandas as pd
import numpy as np

# Define possible values for each feature
genders = ['M', 'F']
ages = np.arange(18, 60)  # Age range from 18 to 60

# Generate random data for users
num_users = 1000
user_data = {
    'user_id': np.arange(1, num_users + 1),
    'gender': np.random.choice(genders, num_users),
    'age': np.random.choice(ages, num_users),
    'waist': np.random.randint(24, 40, num_users),  # Example waist sizes
    'chest': np.random.randint(30, 50, num_users),  # Example chest sizes
    'hip': np.random.randint(30, 50, num_users),    # Example hip sizes
    'shoulder': np.random.randint(14, 22, num_users),  # Example shoulder sizes
    'height': np.random.randint(58, 76, num_users)   # Example height in inches
}

# Convert to DataFrame
user_df = pd.DataFrame(user_data)

# Save to CSV
user_df.to_csv('synthetic_user_data.csv', index=False)

# Save to JSON
user_df.to_json('synthetic_user_data.json', orient='records', lines=True)
