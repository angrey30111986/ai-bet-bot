import os
import joblib
import pandas as pd

from sklearn.ensemble import RandomForestClassifier

from features import create_features


BASE_DIR = os.path.dirname(os.path.abspath(__file__))
MATCHES_FILE = os.path.join(BASE_DIR, "data", "matches.csv")
MODEL_FILE = os.path.join(BASE_DIR, "models", "football_ai.pkl")


def train():

    df = pd.read_csv(MATCHES_FILE)

    df = create_features(df)

    y = df["result"]

    X = df.drop(columns=["result"])

    model = RandomForestClassifier(
        n_estimators=500,
        max_depth=15,
        random_state=42
    )

    model.fit(X, y)

    joblib.dump(model, MODEL_FILE)

    print("Model saved:", MODEL_FILE)


if __name__ == "__main__":
    train()
