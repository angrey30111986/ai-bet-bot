import requests
from config import API_KEY

headers = {
    "x-apisports-key": API_KEY
}

def team_statistics(team, league, season):

    url = "https://v3.football.api-sports.io/teams/statistics"

    params = {
        "team": team,
        "league": league,
        "season": season
    }

    response = requests.get(
        url,
        headers=headers,
        params=params
    )

    return response.json()["response"]
