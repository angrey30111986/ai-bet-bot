import pandas as pd

def create_features(df):

    df["goal_diff"] = df["home_goals"] - df["away_goals"]

    df["total_goals"] = df["home_goals"] + df["away_goals"]

    df["result"] = df["goal_diff"].apply(
        lambda x: 0 if x > 0 else (1 if x == 0 else 2)
    )

    return df
