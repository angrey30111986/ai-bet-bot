import requests
from config import BASE_URL, HEADERS


def get_odds(fixture_id):

    url = f"{BASE_URL}/odds"

    response = requests.get(
        url,
        headers=HEADERS,
        params={
            "fixture": fixture_id
        }
    )

    if response.status_code != 200:
        return None

    data = response.json().get("response", [])

    if not data:
        return None

    try:
        bookmaker = data[0]["bookmakers"][0]
        bet = bookmaker["bets"][0]["values"]

        return {
            "home_odds": float(bet[0]["odd"]),
            "draw_odds": float(bet[1]["odd"]),
            "away_odds": float(bet[2]["odd"])
        }

    except Exception:
        return None
