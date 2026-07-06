import pandas as pd

from elo import get
from form import get_form
from fatigue import days_since_last


def create_features(match):

    home = match["home_team"]
    away = match["away_team"]

    home_elo = get(home)
    away_elo = get(away)

    home_form = get_form(home)
    away_form = get_form(away)

    home_rest = days_since_last(home, match["date"])
    away_rest = days_since_last(away, match["date"])

    return {

        "home_elo": home_elo,
        "away_elo": away_elo,
        "elo_diff": home_elo - away_elo,

        "home_form": home_form,
        "away_form": away_form,
        "form_diff": home_form - away_form,

        "home_rest": home_rest,
        "away_rest": away_rest,
        "rest_diff": home_rest - away_rest

    }
