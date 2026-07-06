import pandas as pd

columns = [
    "home_team",
    "away_team",
    "home_elo",
    "away_elo",
    "home_form",
    "away_form",
    "home_attack",
    "away_attack",
    "home_defense",
    "away_defense",
    "home_goals_avg",
    "away_goals_avg",
    "result"
]

df = pd.DataFrame(columns=columns)

df.to_csv("dataset.csv", index=False)

print("dataset.csv створено")
