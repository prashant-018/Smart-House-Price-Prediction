import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

MODEL_PATH = os.path.join(BASE_DIR, "ml", "model.pkl")
SCALER_PATH = os.path.join(BASE_DIR, "ml", "scaler.pkl")
ENCODER_PATH = os.path.join(BASE_DIR, "ml", "encoder.pkl")