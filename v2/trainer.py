import pandas as pd
import joblib

from catboost import CatBoostClassifier
from features import create_features

df = pd.read_csv("matches.csv")

df = create_features(df)

X = df[[
    "goal_diff",
    "total_goals"
]]

y = df["result"]

model = CatBoostClassifier(
    iterations=500,
    learning_rate=0.05,
    depth=8,
    loss_function="MultiClass",
    verbose=False
)

model.fit(X, y)

joblib.dump(model, "football_ai.pkl")

print("Модель навчена.")
