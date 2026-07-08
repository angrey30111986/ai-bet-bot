"""
AI BET BOT v3
Match Importance
"""


def calculate_importance(match):

    home_rank = match["standings"]["home"].get("rank")
    away_rank = match["standings"]["away"].get("rank")

    home_points = match["standings"]["home"].get("points")
    away_points = match["standings"]["away"].get("points")

    score = 50

    if home_rank and away_rank:

        if home_rank <= 3 or away_rank <= 3:
            score += 20

        if home_rank <= 6 and away_rank <= 6:
            score += 10

        if abs(home_rank - away_rank) <= 2:
            score += 10

    if home_points and away_points:

        if abs(home_points - away_points) <= 5:
            score += 10

    if score > 100:
        score = 100

    match["importance"] = {

        "score": score,

        "level": (
            "HIGH"
            if score >= 80
            else "MEDIUM"
            if score >= 60
            else "LOW"
        )

    }

    return match


if __name__ == "__main__":

    print("Importance module loaded")
