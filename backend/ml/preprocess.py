import pandas as pd
import os

# -----------------------------
# Load Dataset
# -----------------------------
current_dir = os.path.dirname(__file__)
dataset_path = os.path.join(current_dir, "..", "..", "dataset", "train.csv")

df = pd.read_csv(dataset_path)

print("=" * 60)
print("ORIGINAL DATASET")
print("=" * 60)
print("Shape :", df.shape)

# -----------------------------
# Drop Columns (80%+ Missing)
# -----------------------------
drop_columns = [
    "PoolQC",
    "MiscFeature",
    "Alley",
    "Fence"
]

df.drop(columns=drop_columns, inplace=True)

# -----------------------------
# Fill Numerical Missing Values
# -----------------------------
numerical_columns = [
    "LotFrontage",
    "GarageYrBlt",
    "MasVnrArea"
]

for col in numerical_columns:
    df[col] = df[col].fillna(df[col].median())

# -----------------------------
# Fill Categorical Missing Values
# -----------------------------
categorical_columns = [
    "MasVnrType",
    "FireplaceQu",
    "GarageType",
    "GarageFinish",
    "GarageQual",
    "GarageCond",
    "BsmtExposure",
    "BsmtFinType2",
    "BsmtQual",
    "BsmtCond",
    "BsmtFinType1",
    "Electrical"
]

for col in categorical_columns:
    df[col] = df[col].fillna(df[col].mode()[0])

# -----------------------------
# Final Check
# -----------------------------
print("\n" + "=" * 60)
print("DATA CLEANING COMPLETED")
print("=" * 60)

print("\nDataset Shape")
print(df.shape)

print("\nRemaining Missing Values")
print(df.isnull().sum().sum())

print("\nFirst 5 Rows")
print(df.head())

# -----------------------------
# Save Clean Dataset
# -----------------------------
clean_dataset_path = os.path.join(
    current_dir,
    "..",
    "..",
    "dataset",
    "clean_train.csv"
)

df.to_csv(clean_dataset_path, index=False)

print("\nClean dataset saved successfully!")
print(clean_dataset_path)