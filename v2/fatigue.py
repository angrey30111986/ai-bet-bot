from datetime import datetime

last_match = {}


def get_fatigue(home_team, away_team, fixture=None):

    home_rest = 7
    away_rest = 7

    if fixture is not None:

        # Працює і з API-Football, і з matches.csv
        if isinstance(fixture, dict):

            if "fixture" in fixture:
                match_date = fixture["fixture"]["date"]
            else:
                match_date = fixture.get("date")

            if match_date:

                if "T" in str(match_date):
                    current = datetime.fromisoformat(
                        str(match_date).replace("Z", "")
                    )
                else:
                    current = datetime.strptime(
                        str(match_date),
                        "%Y-%m-%d"
                    )

                if home_team in last_match:
                    home_rest = (
                        current - last_match[home_team]
                    ).days

                if away_team in last_match:
                    away_rest = (
                        current - last_match[away_team]
                    ).days

                last_match[home_team] = current
                last_match[away_team] = current

    return {
        "home_rest_days": max(home_rest, 0),
        "away_rest_days": max(away_rest, 0)
    }


def reset():

    last_match.clear()
