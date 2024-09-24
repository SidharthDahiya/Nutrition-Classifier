import pandas as pd
import glob

# Step 1: Load all CSV files
file_paths = glob.glob('/Users/sidharth/PycharmProjects/Personalized Nutrition/Nutrition data/*.csv')  # Update with your actual path

# Load and concatenate all CSV files into a single DataFrame
all_dataframes = []
for file_path in file_paths:
    df = pd.read_csv(file_path)
    all_dataframes.append(df)

# Concatenate all dataframes
nutrition_data = pd.concat(all_dataframes, ignore_index=True)

# Step 2: Feature Selection
# Select relevant features for the nutrition recommendation system
selected_features = [
    'food', 'Caloric Value', 'Fat', 'Saturated Fats', 'Carbohydrates',
    'Sugars', 'Protein', 'Dietary Fiber', 'Cholesterol', 'Sodium',
    'Water', 'Vitamin A', 'Vitamin B12', 'Vitamin C', 'Vitamin D',
    'Vitamin E', 'Vitamin K', 'Copper', 'Magnesium', 'Manganese',
    'Phosphorus', 'Potassium', 'Zinc', 'Nutrition Density'
]
nutrition_selected = nutrition_data[selected_features].copy()

# Step 3: Data Cleaning
# Convert numeric columns to appropriate types
def clean_numeric(column):
    return pd.to_numeric(column.astype(str).str.replace(r'[^\d.]', '', regex=True), errors='coerce')

numeric_columns = ['Caloric Value', 'Fat', 'Saturated Fats',
                   'Carbohydrates', 'Sugars', 'Protein',
                   'Dietary Fiber', 'Cholesterol', 'Sodium',
                   'Water', 'Vitamin A', 'Vitamin B12',
                   'Vitamin C', 'Vitamin D', 'Vitamin E',
                   'Vitamin K', 'Copper', 'Magnesium',
                   'Manganese', 'Phosphorus',
                   'Potassium', 'Zinc',
                   'Nutrition Density']

for column in numeric_columns:
    nutrition_selected[column] = clean_numeric(nutrition_selected[column])

# Fill missing numerical values with the mean of each column
nutrition_selected[numeric_columns] = nutrition_selected[numeric_columns].fillna(nutrition_selected[numeric_columns].mean())

# For categorical data like 'food', fill missing values with a placeholder
nutrition_selected['food'] = nutrition_selected['food'].fillna('Unknown')

# Step 4: Save cleaned data to a new CSV file
cleaned_file_path = '/Users/sidharth/PycharmProjects/Personalized Nutrition/cleaned_nutrition_data.csv'
nutrition_selected.to_csv(cleaned_file_path, index=False)

print(f"Cleaned data saved to {cleaned_file_path}")