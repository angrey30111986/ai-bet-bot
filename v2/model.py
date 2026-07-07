import os
import joblib

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

MODEL_FILE = os.path.join(
    BASE_DIR,
    "models",
    "football_ai.pkl"
)


def load_model():

    if not os.path.exists(MODEL_FILE):
        return None

    return joblib.load(MODEL_FILE)


def save_model(model):

    joblib.dump(model, MODEL_FILE)
