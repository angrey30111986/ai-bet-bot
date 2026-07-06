import pandas as pd

def create_features(df):

    df["goal_diff"] = df["home_goals"] - df["away_goals"]

    df["total_goals"] = df["home_goals"] + df["away_goals"]

    df["home_win"] = (df["home_goals"] > df["away_goals"]).astype(int)

    df["draw"] = (df["home_goals"] == df["away_goals"]).astype(int)

    df["away_win"] = (df["home_goals"] < df["away_goals"]).astype(int)

    return df
