from datetime import datetime

last_match = {}


def days_since_last(team, date):

    current = datetime.fromisoformat(
        date.replace("Z", "+00:00")
    )

    if team not in last_match:

        last_match[team] = current

        return 7

    days = (current - last_match[team]).days

    last_match[team] = current

    return days
