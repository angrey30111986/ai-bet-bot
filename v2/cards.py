import requests
from config import API_KEY

URL = "https://v3.football.api-sports.io/fixtures/events"

HEADERS = {
    "x-apisports-key": API_KEY
}


def get_cards(fixture_id):

    response = requests.get(
        URL,
        headers=HEADERS,
        params={"fixture": fixture_id},
        timeout=20
    )

    if response.status_code != 200:
        return {}

    data = response.json().get("response", [])

    home_yellow = 0
    away_yellow = 0
    home_red = 0
    away_red = 0

    home_team = None
    away_team = None

    for event in data:

        if event.get("type") != "Card":
            continue

        if home_team is None:
            home_team = event["team"]["id"]

        if event["team"]["id"] == home_team:

            if event["detail"] == "Yellow Card":
                home_yellow += 1

            elif "Red" in event["detail"]:
                home_red += 1

        else:

            away_team = event["team"]["id"]

            if event["detail"] == "Yellow Card":
                away_yellow += 1

            elif "Red" in event["detail"]:
                away_red += 1

    return {
        "home_yellow": home_yellow,
        "away_yellow": away_yellow,
        "home_red": home_red,
        "away_red": away_red
    }
