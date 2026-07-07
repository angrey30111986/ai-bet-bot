import os
import joblib
import pandas as pd

from sklearn.ensemble import RandomForestClassifier
from features import create_features

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_FILE = os.path.join(BASE_DIR, "data", "matches.csv")
MODEL_FILE = os.path.join(BASE_DIR, "models", "football_ai.pkl")


def train():

    df = pd.read_csv(DATA_FILE)

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

    print("MODEL SAVED")


if __name__ == "__main__":
    train()
