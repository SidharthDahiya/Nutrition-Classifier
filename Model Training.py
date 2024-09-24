import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score
import pickle

# Step 1: Load the cleaned nutrition data
data = pd.read_csv('cleaned_nutrition_data.csv')

# Step 2: Preprocess the Data
# Convert 'Nutrition Density' to categorical by binning into classes (e.g., low, medium, high)
data['Nutrition Density Category'] = pd.qcut(data['Nutrition Density'], q=3, labels=[0, 1, 2])

# Define features (X) and target (y)
features = data.drop(columns=['food', 'Nutrition Density', 'Nutrition Density Category'])
target = data['Nutrition Density Category']

# Step 3: Split the Data
X_train, X_test, y_train, y_test = train_test_split(features, target, test_size=0.2, random_state=42)

# Step 4: Choose and Train a Model
model = DecisionTreeClassifier(random_state=42)
model.fit(X_train, y_train)

# Step 5: Evaluate the Model
y_pred = model.predict(X_test)
accuracy = accuracy_score(y_test, y_pred)
print(f'Model Accuracy: {accuracy:.2f}')

# Save the trained model to a file named 'best_model.pkl'
with open('best_model.pkl', 'wb') as f:
    pickle.dump(model, f)

print("Model saved as 'best_model.pkl'")