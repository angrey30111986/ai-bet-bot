import pandas as pd
from elo import get_elo
from fatigue import get_fatigue


def create_features(df):

    rows = []

    for _, match in df.iterrows():

        home = str(match["home_team"])
        away = str(match["away_team"])

        elo = get_elo(home, away)
        fatigue = get_fatigue(home, away)

        rows.append({

            "home_elo": elo["home_elo"],
            "away_elo": elo["away_elo"],
            "elo_diff": elo["elo_diff"],

            "home_rest": fatigue["home_rest_days"],
            "away_rest": fatigue["away_rest_days"],
            "rest_diff": fatigue["home_rest_days"] - fatigue["away_rest_days"],

            "home_goals": int(match["home_goals"]),
            "away_goals": int(match["away_goals"]),

            "goal_diff": int(match["home_goals"]) - int(match["away_goals"]),
            "total_goals": int(match["home_goals"]) + int(match["away_goals"]),

            "result": int(match["result"])

        })

    return pd.DataFrame(rows)
