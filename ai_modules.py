# Example: AI Prediction Model (Scikit-learn)

from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
import pandas as pd

# Load your cleaned health dataset
data = pd.read_csv('health_data.csv')

# Split data into features and target variable
X = data.drop('epidemic_label', axis=1)  # Features
y = data['epidemic_label']  # Target variable (epidemic yes/no)

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train the AI model
model = RandomForestClassifier()
model.fit(X_train, y_train)

# Test the model
y_pred = model.predict(X_test)
accuracy = accuracy_score(y_test, y_pred)
print(f"Model accuracy: {accuracy}")

# The trained model can be used to predict new outbreaks
