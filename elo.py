import pandas as pd

ratings = {}

START_ELO = 1500

K = 20


def get(team):

    if team not in ratings:
        ratings[team] = START_ELO

    return ratings[team]


def update(home, away, result):

    home_elo = get(home)
    away_elo = get(away)

    expected_home = 1 / (1 + 10 ** ((away_elo-home_elo)/400))
    expected_away = 1 - expected_home

    if result == 1:
        score_home = 1
        score_away = 0

    elif result == 0:
        score_home = 0.5
        score_away = 0.5

    else:
        score_home = 0
        score_away = 1

    ratings[home] = home_elo + K*(score_home-expected_home)
    ratings[away] = away_elo + K*(score_away-expected_away)
