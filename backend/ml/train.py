import pandas as pd
import os

# Current directory
current_dir = os.path.dirname(__file__)

# Dataset path
dataset_path = os.path.join(current_dir, "..", "..", "dataset", "train.csv")

# Load dataset
df = pd.read_csv(dataset_path)

print("=" * 60)
print("HOUSE PRICE PREDICTION DATASET")
print("=" * 60)

# Dataset Shape
print("\n1. Dataset Shape")
print(df.shape)

# First 5 Rows
print("\n2. First 5 Rows")
print(df.head())

# Column Names
print("\n3. Column Names")
print(df.columns.tolist())

# Dataset Information
print("\n4. Dataset Information")
df.info()

# Missing Values
print("\n5. Missing Values")
print(df.isnull().sum())

# Statistical Summary
print("\n6. Statistical Summary")
print(df.describe())

# Missing Value Percentage
print("\n" + "=" * 60)
print("7. MISSING VALUE PERCENTAGE")
print("=" * 60)

missing = (df.isnull().sum() / len(df)) * 100
missing = missing[missing > 0].sort_values(ascending=False)

print(missing)

# Target Column Statistics
print("\n" + "=" * 60)
print("8. TARGET COLUMN (SalePrice)")
print("=" * 60)

print(df["SalePrice"].describe())

# Numeric Columns
print("\n" + "=" * 60)
print("9. NUMERIC COLUMNS")
print("=" * 60)

numeric_columns = df.select_dtypes(include=["int64", "float64"]).columns
print(numeric_columns.tolist())

# Categorical Columns
print("\n" + "=" * 60)
print("10. CATEGORICAL COLUMNS")
print("=" * 60)

categorical_columns = df.select_dtypes(include=["object"]).columns
print(categorical_columns.tolist())

# Duplicate Rows
print("\n" + "=" * 60)
print("11. DUPLICATE ROWS")
print("=" * 60)

print(df.duplicated().sum())