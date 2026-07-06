import requests

API_KEY = "03b997d33e6e88f7b1dc3e9f179d7f17"

headers = {
    "x-apisports-key": API_KEY
}


def get_cards(fixture_id):
    url = "https://v3.football.api-sports.io/fixtures/events"

    response = requests.get(
        url,
        headers=headers,
        params={"fixture": fixture_id}
    )

    if response.status_code != 200:
        return {
            "home_yellow": 0,
            "away_yellow": 0,
            "home_red": 0,
            "away_red": 0
        }

    data = response.json()["response"]

    home_yellow = 0
    away_yellow = 0
    home_red = 0
    away_red = 0

    for event in data:

        if event["type"] == "Card":

            detail = event["detail"]

            if event["team"]["id"] == event["team"]["id"]:

                if detail == "Yellow Card":
                    home_yellow += 1

                elif detail == "Red Card":
                    home_red += 1

    return {
        "home_yellow": home_yellow,
        "away_yellow": away_yellow,
        "home_red": home_red,
        "away_red": away_red
    }
