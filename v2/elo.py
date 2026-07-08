from collections import defaultdict

ratings = defaultdict(lambda: 1500)

K = 20


def expected(a, b):
    return 1 / (1 + 10 ** ((b - a) / 400))


def update(home, away, result):

    ra = ratings[home]
    rb = ratings[away]

    ea = expected(ra, rb)
    eb = expected(rb, ra)

    if result == 0:
        sa = 1
        sb = 0
    elif result == 1:
        sa = 0.5
        sb = 0.5
    else:
        sa = 0
        sb = 1

    ratings[home] = ra + K * (sa - ea)
    ratings[away] = rb + K * (sb - eb)


def build_elo(df):

    ratings.clear()

    for _, match in df.iterrows():

        home = match["home_team"]
        away = match["away_team"]
        result = match["result"]

        update(home, away, result)


def get_elo(home_team, away_team):

    home = ratings[home_team]
    away = ratings[away_team]

    return {
        "home_elo": round(home, 2),
        "away_elo": round(away, 2),
        "elo_diff": round(home - away, 2)
    }
