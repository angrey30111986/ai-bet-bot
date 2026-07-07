import os
import pandas as pd

# Шлях до папки data
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_DIR = os.path.join(BASE_DIR, "data")
MATCHES_FILE = os.path.join(DATA_DIR, "matches.csv")

REQUIRED_COLUMNS = [
    "date",
    "league",
    "home_team",
    "away_team",
    "home_goals",
    "away_goals",
    "result"
]


def load_matches():
    """
    Завантажити історію матчів.
    """

    if not os.path.exists(MATCHES_FILE):
        raise FileNotFoundError(
            f"Не знайдено файл {MATCHES_FILE}"
        )

    df = pd.read_csv(MATCHES_FILE)

    if df.empty:
        print("Увага: matches.csv поки порожній.")
        return df

    for column in REQUIRED_COLUMNS:
        if column not in df.columns:
            raise Exception(
                f"Відсутня колонка: {column}"
            )

    return df


def matches_count():
    """
    Кількість матчів.
    """

    df = load_matches()

    return len(df)


def leagues():
    """
    Список ліг.
    """

    df = load_matches()

    if df.empty:
        return []

    return sorted(df["league"].unique())


def teams():
    """
    Список команд.
    """

    df = load_matches()

    if df.empty:
        return []

    home = list(df["home_team"].unique())
    away = list(df["away_team"].unique())

    return sorted(list(set(home + away)))


if __name__ == "__main__":

    data = load_matches()

    print(data.head())

    print()

    print("Матчів:", matches_count())

    print("Команд:", len(teams()))

    print("Ліг:", len(leagues()))
