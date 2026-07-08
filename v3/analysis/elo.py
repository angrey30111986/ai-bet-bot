"""
AI BET BOT v3
ELO Rating
"""


def calculate_elo(match):

    home_rank = match["standings"]["home"].get("rank")
    away_rank = match["standings"]["away"].get("rank")

    if home_rank is None or away_rank is None:

        match["elo"] = {
            "home": 50,
            "away": 50
        }

        return match

    max_rank = max(home_rank, away_rank)

    home_score = round(
        ((max_rank - home_rank + 1) / max_rank) * 100,
        2
    )

    away_score = round(
        ((max_rank - away_rank + 1) / max_rank) * 100,
        2
    )

    match["elo"] = {

        "home": home_score,

        "away": away_score

    }

    return match


def winner(match):

    if match["elo"]["home"] > match["elo"]["away"]:

        return "HOME"

    if match["elo"]["away"] > match["elo"]["home"]:

        return "AWAY"

    return "DRAW"


if __name__ == "__main__":

    print("ELO module loaded")
