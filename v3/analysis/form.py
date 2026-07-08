"""
AI BET BOT v3
Team Form Analysis
"""


def calculate_form(match):

    standings = match.get("standings", {})

    home = standings.get("home", {})
    away = standings.get("away", {})

    home_played = home.get("played") or 0
    away_played = away.get("played") or 0

    home_points = home.get("points") or 0
    away_points = away.get("points") or 0

    home_form = 0
    away_form = 0

    if home_played > 0:
        home_form = round(
            (home_points / (home_played * 3)) * 100,
            2
        )

    if away_played > 0:
        away_form = round(
            (away_points / (away_played * 3)) * 100,
            2
        )

    match["form"] = {

        "home": {
            "score": home_form,
            "played": home_played,
            "points": home_points
        },

        "away": {
            "score": away_form,
            "played": away_played,
            "points": away_points
        }

    }

    return match


def winner(match):

    home = match["form"]["home"]["score"]
    away = match["form"]["away"]["score"]

    if home > away:
        return "HOME"

    if away > home:
        return "AWAY"

    return "DRAW"


if __name__ == "__main__":

    print("Form module loaded")
