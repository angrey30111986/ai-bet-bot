"""
AI BET BOT v3
Fatigue Analysis
"""

from datetime import datetime


def calculate_fatigue(match):

    fixture_date = match.get("date")

    if not fixture_date:

        match["fatigue"] = {
            "home": 50,
            "away": 50
        }

        return match

    fixture_time = datetime.fromisoformat(
        fixture_date.replace("Z", "+00:00")
    )

    now = datetime.now(fixture_time.tzinfo)

    days = (fixture_time - now).days

    score = 100

    if days <= 2:
        score = 55

    elif days <= 4:
        score = 70

    elif days <= 6:
        score = 85

    match["fatigue"] = {
        "home": score,
        "away": score
    }

    return match
