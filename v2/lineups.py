import requests
from config import BASE_URL, HEADERS


def get_lineup(fixture_id):

    url = f"{BASE_URL}/fixtures/lineups"

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

    if len(data) < 2:
        return None

    home = data[0]
    away = data[1]

    return {
        "home_formation": home.get("formation", ""),
        "away_formation": away.get("formation", ""),
        "home_coach": home.get("coach", {}).get("name", ""),
        "away_coach": away.get("coach", {}).get("name", ""),
        "home_starting": len(home.get("startXI", [])),
        "away_starting": len(away.get("startXI", []))
    }
