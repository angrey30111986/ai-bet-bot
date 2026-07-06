import pandas as pd
import joblib

from catboost import CatBoostClassifier

from dataset import build_dataset


# Завантаження матчів
df = pd.read_csv("matches.csv")

# Побудова датасету
df = build_dataset(df)

# Ознаки
features = [
    "home_elo",
    "away_elo",
    "elo_diff",
    "home_rest",
    "away_rest",
    "rest_diff"
]

X = df[features]
y = df["result"]

# Навчання моделі
model = CatBoostClassifier(
    iterations=1000,
    learning_rate=0.03,
    depth=8,
    loss_function="MultiClass",
    verbose=100
)

model.fit(X, y)

# Збереження моделі
joblib.dump(model, "football_ai.pkl")

print("Навчання завершено!")
