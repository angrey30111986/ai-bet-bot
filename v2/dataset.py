import pandas as pd

from elo import get, update
from fatigue import days_since_last


def build_dataset(df):

    df = df.sort_values("date").reset_index(drop=True)

    rows = []

    for _, match in df.iterrows():

        home = match["home_team"]
        away = match["away_team"]

        home_elo = get(home)
        away_elo = get(away)

        home_rest = days_since_last(home, match["date"])
        away_rest = days_since_last(away, match["date"])

        if match["home_goals"] > match["away_goals"]:
            result = 0
        elif match["home_goals"] < match["away_goals"]:
            result = 2
        else:
            result = 1

        rows.append({
            "home_team": home,
            "away_team": away,

            "home_elo": home_elo,
            "away_elo": away_elo,
            "elo_diff": home_elo - away_elo,

            "home_rest": home_rest,
            "away_rest": away_rest,
            "rest_diff": home_rest - away_rest,

            "home_goals": match["home_goals"],
            "away_goals": match["away_goals"],

            "result": result
        })

        update(home, away, result)

    return pd.DataFrame(rows)
