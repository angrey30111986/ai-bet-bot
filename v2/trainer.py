import os
import joblib
import pandas as pd

from sklearn.ensemble import RandomForestClassifier
from features import create_features

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

DATA_FILE = os.path.join(BASE_DIR, "data", "matches.csv")
MODEL_DIR = os.path.join(BASE_DIR, "models")
MODEL_FILE = os.path.join(MODEL_DIR, "football_ai.pkl")


def train():

    if not os.path.exists(DATA_FILE):
        raise FileNotFoundError(f"Dataset not found: {DATA_FILE}")

    os.makedirs(MODEL_DIR, exist_ok=True)

    df = pd.read_csv(DATA_FILE)

    if len(df) < 10:
        raise Exception("Not enough matches for training")

    features = create_features(df)

    y = features.pop("result")

    model = RandomForestClassifier(
        n_estimators=500,
        max_depth=20,
        min_samples_leaf=2,
        random_state=42,
        n_jobs=-1
    )

    model.fit(features, y)

    joblib.dump(model, MODEL_FILE)

    print("=" * 40)
    print("MODEL SAVED")
    print("MODEL PATH:", MODEL_FILE)
    print("FILE EXISTS:", os.path.exists(MODEL_FILE))

    if os.path.exists(MODEL_FILE):
        print("FILE SIZE:", os.path.getsize(MODEL_FILE), "bytes")
    print("=" * 40)


if __name__ == "__main__":
    train()
