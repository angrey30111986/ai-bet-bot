import requests
from config import BASE_URL, HEADERS


def get_standings(league_id, season, team_id):

    url = f"{BASE_URL}/standings"

    response = requests.get(
        url,
        headers=HEADERS,
        params={
            "league": league_id,
            "season": season
        }
    )

    if response.status_code != 200:
        return None

    data = response.json().get("response", [])

    if not data:
        return None

    try:
        standings = data[0]["league"]["standings"][0]

        for team in standings:
            if team["team"]["id"] == team_id:
                return {
                    "rank": team["rank"],
                    "points": team["points"],
                    "goals_diff": team["goalsDiff"],
                    "played": team["all"]["played"],
                    "wins": team["all"]["win"],
                    "draws": team["all"]["draw"],
                    "losses": team["all"]["lose"]
                }

    except Exception:
        return None

    return None
