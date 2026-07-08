from datetime import datetime

last_match = {}


def days_since_last(team, match_date):

    current = datetime.fromisoformat(
        match_date.replace("Z", "+00:00")
    )

    if team not in last_match:
        last_match[team] = current
        return 7

    days = (current - last_match[team]).days

    last_match[team] = current

    if days < 0:
        days = 0

    return days


def get_fatigue(home_team, away_team, fixture=None):

    if fixture is None:

        return {
            "home_rest_days": 7,
            "away_rest_days": 7
        }

    match_date = fixture["fixture"]["date"]

    return {
        "home_rest_days": days_since_last(home_team, match_date),
        "away_rest_days": days_since_last(away_team, match_date)
    }
