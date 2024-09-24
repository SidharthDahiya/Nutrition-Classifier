# Nutrition Classifier

This project is an ML based system designed to predict the 'Nutrition Density' of various food items using nutritional features. The model is trained to classify food items into categories based on their nutritional content.

## Project Overview

The goal of this project is to provide personalized nutrition recommendations by predicting the nutrition density of different food items. The model is trained using a dataset containing various nutritional features such as caloric value, fat content, vitamins, and minerals.

### Features and Labels

- **Features**: The input features used by the model include:
  - Caloric Value
  - Fat
  - Saturated Fats
  - Carbohydrates
  - Sugars
  - Protein
  - Dietary Fiber
  - Cholesterol
  - Sodium
  - Water
  - Vitamins (A, B12, C, D, E, K)
  - Minerals (Copper, Magnesium, Manganese, Phosphorus, Potassium, Zinc)

- **Label**: The target label for prediction is 'Nutrition Density', which is categorized into classes (e.g., low, medium, high)

## Dataset

The dataset used for this project is `cleaned_nutrition_data.csv`, which includes detailed nutritional information for various food items.
Link for Kaggle Dataset used - https://www.kaggle.com/datasets/utsavdey1410/food-nutrition-dataset

## Model Training
The provided Python script (Model_Training.py) outlines the process of training a machine learning model to predict 'Nutrition Density' using a Decision Tree Classifier. It involves loading and preprocessing nutritional data, where features like caloric value, fat, and carbohydrates are used to predict the categorical label 'Nutrition Density'. The dataset is split into training and testing sets, and the model is evaluated for accuracy before being saved for future predictions.

## Evaluation
The model's performance is evaluated using accuracy metrics. The current model achieves an accuracy of approximately 81%.

## Tools and Libraries
This project utilizes the following tools and libraries:
- Python
- Pandas
- Scikit-learn
- Flask
  
## Next Steps
In future iterations of this project, we plan to integrate user-specific data such as weight, height, BMI, etc., to provide more precise dietary recommendations. By incorporating these personal metrics along with nutritional values, the system can suggest meal plans that meet specific dietary requirements or health goals.
