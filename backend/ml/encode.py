import pandas as pd
import os
import joblib

from sklearn.preprocessing import LabelEncoder

# -----------------------------
# Load Clean Dataset
# -----------------------------
current_dir = os.path.dirname(__file__)

dataset_path = os.path.join(
    current_dir,
    "..",
    "..",
    "dataset",
    "clean_train.csv"
)

df = pd.read_csv(dataset_path)

print("=" * 60)
print("ENCODING STARTED")
print("=" * 60)

# Store all encoders
encoders = {}

# Find categorical columns
categorical_columns = df.select_dtypes(include=["object"]).columns

# Encode every categorical column
for col in categorical_columns:
    le = LabelEncoder()
    df[col] = le.fit_transform(df[col].astype(str))
    encoders[col] = le

print("\nCategorical Columns Encoded :", len(categorical_columns))

# Save encoded dataset
encoded_path = os.path.join(
    current_dir,
    "..",
    "..",
    "dataset",
    "encoded_train.csv"
)

df.to_csv(encoded_path, index=False)

# Save encoders
encoder_path = os.path.join(current_dir, "encoder.pkl")
joblib.dump(encoders, encoder_path)

print("\nEncoded Dataset Saved Successfully")
print(encoded_path)

print("\nEncoder Saved Successfully")
print(encoder_path)

print("\nDataset Shape")
print(df.shape)