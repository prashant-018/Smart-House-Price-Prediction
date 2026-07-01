import os
import joblib

from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error
from sklearn.metrics import mean_squared_error
from sklearn.metrics import r2_score
import numpy as np

print("=" * 60)
print("LINEAR REGRESSION MODEL TRAINING")
print("=" * 60)

current_dir = os.path.dirname(__file__)

# Load Train/Test Data
X_train = joblib.load(os.path.join(current_dir, "X_train.pkl"))
X_test = joblib.load(os.path.join(current_dir, "X_test.pkl"))
y_train = joblib.load(os.path.join(current_dir, "y_train.pkl"))
y_test = joblib.load(os.path.join(current_dir, "y_test.pkl"))

# Train Model
model = LinearRegression()
model.fit(X_train, y_train)

# Prediction
predictions = model.predict(X_test)

# Metrics
mae = mean_absolute_error(y_test, predictions)
mse = mean_squared_error(y_test, predictions)
rmse = np.sqrt(mse)
r2 = r2_score(y_test, predictions)

print("\nModel Evaluation")
print("-" * 40)
print(f"MAE      : {mae:.2f}")
print(f"MSE      : {mse:.2f}")
print(f"RMSE     : {rmse:.2f}")
print(f"R2 Score : {r2:.4f}")

# Save Model
model_path = os.path.join(current_dir, "model.pkl")
joblib.dump(model, model_path)

print("\nModel Saved Successfully!")
print(model_path)