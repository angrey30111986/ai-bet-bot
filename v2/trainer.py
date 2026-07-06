import pandas as pd
import joblib

from catboost import CatBoostClassifier
from features import create_features

print("Loading matches...")

df = pd.read_csv("matches.csv")

df = create_features(df)

features = [
    "home_form",
    "away_form",
    "home_attack",
    "away_attack"
]

X = df[features].fillna(0)

y = df["result"]

print("Training AI...")

model = CatBoostClassifier(
    iterations=1000,
    learning_rate=0.03,
    depth=8,
    loss_function="MultiClass",
    verbose=100
)

model.fit(X, y)

joblib.dump(model, "football_ai.pkl")

print("AI model saved.")
