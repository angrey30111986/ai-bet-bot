from elo import get

from form import form

def features(home, away):

    return {

        "home_elo": get(home),

        "away_elo": get(away),

        "elo_diff": get(home)-get(away),

        "home_form": form(home),

        "away_form": form(away),

        "form_diff": form(home)-form(away)

    }
