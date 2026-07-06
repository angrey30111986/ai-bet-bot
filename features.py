import pandas as pd


def create_features(df):

    df["goal_diff"] = df["home_goals"] - df["away_goals"]

    df["total_goals"] = df["home_goals"] + df["away_goals"]

    return df
