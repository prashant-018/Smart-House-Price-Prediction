import pandas as pd
import os

print("=" * 60)
print("FEATURE SELECTION")
print("=" * 60)

# Paths
current_dir = os.path.dirname(__file__)
dataset_path = os.path.join(current_dir, "..", "..", "dataset", "clean_train.csv")

# Load Dataset
df = pd.read_csv(dataset_path)

print("\nOriginal Shape :", df.shape)

# Top Important Features
selected_features = [
    "OverallQual",
    "GrLivArea",
    "GarageCars",
    "GarageArea",
    "TotalBsmtSF",
    "FullBath",
    "YearBuilt",
    "YearRemodAdd",
    "LotArea",
    "BedroomAbvGr",
    "SalePrice"
]

# Select Columns
df = df[selected_features]

print("\nSelected Features")
print(df.columns.tolist())

print("\nNew Shape :", df.shape)

# Save Dataset
save_path = os.path.join(current_dir, "..", "..", "dataset", "final_train.csv")
df.to_csv(save_path, index=False)

print("\nFinal Dataset Saved Successfully!")
print(save_path)