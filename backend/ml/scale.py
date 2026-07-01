import pandas as pd
import os
import joblib

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler

print("=" * 60)
print("FEATURE SCALING")
print("=" * 60)

# Path
current_dir = os.path.dirname(__file__)
dataset_path = os.path.join(current_dir, "..", "..", "dataset", "final_train.csv")

# Load Dataset
df = pd.read_csv(dataset_path)

# Features & Target
X = df.drop("SalePrice", axis=1)
y = df["SalePrice"]

print("Features Shape :", X.shape)
print("Target Shape :", y.shape)

# Train Test Split
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)

print("\nTrain Shape :", X_train.shape)
print("Test Shape :", X_test.shape)

# Scaling
scaler = StandardScaler()

X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)

# Save Scaler
scaler_path = os.path.join(current_dir, "scaler.pkl")
joblib.dump(scaler, scaler_path)

print("\nScaler Saved Successfully!")
print(scaler_path)

# Save Train/Test
joblib.dump(X_train, os.path.join(current_dir, "X_train.pkl"))
joblib.dump(X_test, os.path.join(current_dir, "X_test.pkl"))
joblib.dump(y_train, os.path.join(current_dir, "y_train.pkl"))
joblib.dump(y_test, os.path.join(current_dir, "y_test.pkl"))

print("\nScaling Completed Successfully!")