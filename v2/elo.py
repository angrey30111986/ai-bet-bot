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


def reset():
    ratings.clear()


def get_elo(home, away):

    return {
        "home_elo": ratings[home],
        "away_elo": ratings[away],
        "elo_diff": ratings[home] - ratings[away]
    }


def process_match(home, away, result):

    elo = get_elo(home, away)

    update(home, away, result)

    return elo
