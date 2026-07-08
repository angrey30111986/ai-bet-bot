"""
AI BET BOT v3
Model Trainer
"""

import joblib
import pandas as pd

from pathlib import Path

from sklearn.ensemble import RandomForestClassifier

from config import MODEL_PATH


FEATURE = "result"


def train(dataset_path):

    dataset_path = Path(dataset_path)

    if not dataset_path.exists():
        raise FileNotFoundError(dataset_path)

    df = pd.read_csv(dataset_path)

    X = df.drop(columns=[FEATURE])

    y = df[FEATURE]

    model = RandomForestClassifier(

        n_estimators=500,
        max_depth=20,
        min_samples_leaf=2,
        random_state=42,
        n_jobs=-1

    )

    model.fit(X, y)

    Path(MODEL_PATH).parent.mkdir(
        parents=True,
        exist_ok=True
    )

    joblib.dump(model, MODEL_PATH)

    print("Model saved:", MODEL_PATH)

    return model


if __name__ == "__main__":

    train("data/dataset.csv")
