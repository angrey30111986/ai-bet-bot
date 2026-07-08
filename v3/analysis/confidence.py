"""
AI BET BOT v3
Confidence Calculator
"""


def calculate_confidence(match):

    score = 50

    # FORM
    if match["form"]["home"]["score"] > match["form"]["away"]["score"]:
        score += 8

    elif match["form"]["away"]["score"] > match["form"]["home"]["score"]:
        score += 8

    # ELO
    if abs(match["elo"]["home"] - match["elo"]["away"]) >= 15:
        score += 10

    # H2H
    if match["h2h"]["matches"] >= 5:
        score += 5

    # INJURIES
    home_inj = len(match["injuries"]["home"])
    away_inj = len(match["injuries"]["away"])

    if abs(home_inj - away_inj) >= 2:
        score += 5

    # ODDS
    if (
        match["odds"]["home"] and
        match["odds"]["away"]
    ):

        diff = abs(
            match["odds"]["home"] -
            match["odds"]["away"]
        )

        if diff >= 1:
            score += 10

    # IMPORTANCE
    score += match["importance"]["score"] / 10

    if score > 100:
        score = 100

    match["confidence"] = round(score, 2)

    return match


def is_safe(match):

    return match["confidence"] >= 80


if __name__ == "__main__":

    print("Confidence module loaded")
