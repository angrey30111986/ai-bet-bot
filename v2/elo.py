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
        sa, sb = 1, 0
    elif result == 1:
        sa, sb = 0.5, 0.5
    else:
        sa, sb = 0, 1

    ratings[home] += K * (sa - ea)
    ratings[away] += K * (sb - eb)


def get_elo(home_team, away_team):
    return {
        "home_elo": ratings[home_team],
        "away_elo": ratings[away_team],
        "elo_diff": ratings[home_team] - ratings[away_team]
    }
