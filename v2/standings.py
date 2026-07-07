import requests
from config import API_KEY

URL = "https://v3.football.api-sports.io/standings"

HEADERS = {
    "x-apisports-key": API_KEY
}


def get_standings(league_id, season):
    response = requests.get(
        URL,
        headers=HEADERS,
        params={
            "league": league_id,
            "season": season
        },
        timeout=20
    )

    if response.status_code != 200:
        return None

    data = response.json()

    if not data["response"]:
        return None

    return data["response"][0]["league"]["standings"][0]


if __name__ == "__main__":
    table = get_standings(39, 2025)

    if table:
        for team in table[:5]:
            print(
                team["rank"],
                team["team"]["name"],
                team["points"]
            )
