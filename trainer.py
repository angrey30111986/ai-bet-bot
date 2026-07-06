import pandas as pd
import joblib

from catboost import CatBoostClassifier

from engine import build_features

df = pd.read_csv("matches.csv")

df = build_features(df)

features = [
    "goal_diff",
    "total_goals",
    "home_attack",
    "away_attack",
    "home_defense",
    "away_defense",
    "home_points",
    "away_points"
]

X = df[features]
y = df["result"]

model = CatBoostClassifier(
    iterations=1000,
    depth=8,
    learning_rate=0.03,
    loss_function="MultiClass",
    verbose=100
)

model.fit(X, y)

joblib.dump(model, "football_ai.pkl")

print("Навчання завершено")
