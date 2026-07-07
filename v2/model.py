import os
import joblib

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
MODEL_FILE = os.path.join(BASE_DIR, "models", "football_ai.pkl")

print("MODEL PATH:", MODEL_FILE)
print("EXISTS:", os.path.exists(MODEL_FILE))

def load_model():
    if not os.path.exists(MODEL_FILE):
        return None
    return joblib.load(MODEL_FILE)
