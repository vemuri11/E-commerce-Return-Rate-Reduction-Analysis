import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
import joblib
import os

# Ensure models folder exists
os.makedirs("models", exist_ok=True)

# Load dataset
df = pd.read_csv("data/online_retail_II_cleaned.csv")

# Add TotalPrice feature
df["TotalPrice"] = df["Quantity"] * df["UnitPrice"]

# Prepare features and labels
X = df[["Quantity", "UnitPrice", "TotalPrice"]]
y = df["Returned"]

# Split the dataset
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train RandomForest model
model = RandomForestClassifier()
model.fit(X_train, y_train)

# Save the trained model
joblib.dump(model, "models/return_predictor.pkl")
print("✅ Model saved to models/return_predictor.pkl")
