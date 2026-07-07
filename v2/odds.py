import requests
from config import API_KEY

URL = "https://v3.football.api-sports.io/odds"

HEADERS = {
    "x-apisports-key": API_KEY
}


def get_odds(fixture_id):
    response = requests.get(
        URL,
        headers=HEADERS,
        params={
            "fixture": fixture_id
        },
        timeout=20
    )

    if response.status_code != 200:
        return None

    data = response.json()

    if not data["response"]:
        return None

    return data["response"]


if __name__ == "__main__":
    odds = get_odds(1035038)

    print(odds)
