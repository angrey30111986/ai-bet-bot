import pandas as pd
import joblib

from sklearn.ensemble import RandomForestClassifier

from features import create_features

# Завантаження матчів
df = pd.read_csv("matches.csv")

# Створення ознак
df = create_features(df)

# Ціль
y = df["result"]

# Ознаки
X = df.drop(columns=["result"])

# Навчання моделі
model = RandomForestClassifier(
    n_estimators=500,
    max_depth=15,
    random_state=42,
    n_jobs=-1
)

model.fit(X, y)

# Збереження
joblib.dump(model, "football_ai.pkl")

print("Модель навчена!")
