from collections import defaultdict

rating = defaultdict(lambda: 1500)

def expected(a, b):
    return 1 / (1 + 10 ** ((b - a) / 400))

def update(home, away, result):

    home_rating = rating[home]
    away_rating = rating[away]

    exp_home = expected(home_rating, away_rating)
    exp_away = expected(away_rating, home_rating)

    k = 20

    if result == 1:
        s_home = 1
        s_away = 0
    elif result == 0:
        s_home = 0.5
        s_away = 0.5
    else:
        s_home = 0
        s_away = 1

    rating[home] += k * (s_home - exp_home)
    rating[away] += k * (s_away - exp_away)
