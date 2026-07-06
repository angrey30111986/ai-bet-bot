import pandas as pd

def build_features(matches):

    df = matches.copy()

    df["goal_diff"] = df["home_goals"] - df["away_goals"]

    df["total_goals"] = df["home_goals"] + df["away_goals"]

    df["home_attack"] = df["home_goals"]

    df["away_attack"] = df["away_goals"]

    df["home_defense"] = df["away_goals"]

    df["away_defense"] = df["home_goals"]

    df["home_points"] = (
        (df["result"] == 1) * 3 +
        (df["result"] == 0)
    )

    df["away_points"] = (
        (df["result"] == 2) * 3 +
        (df["result"] == 0)
    )

    return df
