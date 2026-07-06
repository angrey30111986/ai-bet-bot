import pandas as pd

def create_features(df):

    df = df.sort_values("date").reset_index(drop=True)

    home_form = []
    away_form = []

    home_attack = []
    away_attack = []

    history = {}

    for _, row in df.iterrows():

        home = row["home_team"]
        away = row["away_team"]

        if home not in history:
            history[home] = []

        if away not in history:
            history[away] = []

        home_games = history[home][-5:]
        away_games = history[away][-5:]

        if len(home_games) == 0:
            home_form.append(0)
            home_attack.append(0)
        else:
            home_form.append(sum(home_games) / len(home_games))
            home_attack.append(
                sum(g["scored"] for g in home_games) / len(home_games)
            )

        if len(away_games) == 0:
            away_form.append(0)
            away_attack.append(0)
        else:
            away_form.append(sum(away_games) / len(away_games))
            away_attack.append(
                sum(g["scored"] for g in away_games) / len(away_games)
            )

        if row["home_goals"] > row["away_goals"]:
            home_points = 3
            away_points = 0
        elif row["home_goals"] < row["away_goals"]:
            home_points = 0
            away_points = 3
        else:
            home_points = 1
            away_points = 1

        history[home].append({
            "points": home_points,
            "scored": row["home_goals"]
        })

        history[away].append({
            "points": away_points,
            "scored": row["away_goals"]
        })

    df["home_form"] = home_form
    df["away_form"] = away_form

    df["home_attack"] = home_attack
    df["away_attack"] = away_attack

    df["result"] = df.apply(
        lambda x: 0 if x.home_goals > x.away_goals
        else 1 if x.home_goals == x.away_goals
        else 2,
        axis=1
    )

    return df
