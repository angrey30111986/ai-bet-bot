import os
import pandas as pd

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
MATCHES_FILE = os.path.join(BASE_DIR, "data", "matches.csv")

REQUIRED_COLUMNS = [
    "date",
    "home_team",
    "away_team",
    "home_goals",
    "away_goals",
    "result"
]


def load_dataset():

    if not os.path.exists(MATCHES_FILE):
        raise FileNotFoundError(MATCHES_FILE)

    df = pd.read_csv(MATCHES_FILE)

    if df.empty:
        raise ValueError("matches.csv is empty")

    missing = [
        c for c in REQUIRED_COLUMNS
        if c not in df.columns
    ]

    if missing:
        raise ValueError(
            "Missing columns: " + ", ".join(missing)
        )

    df["date"] = pd.to_datetime(df["date"])

    df = df.sort_values("date").reset_index(drop=True)

    return df


def save_dataset(df):

    df.to_csv(
        MATCHES_FILE,
        index=False
    )


if __name__ == "__main__":

    data = load_dataset()

    print(data.head())

    print()

    print("Matches:", len(data))
