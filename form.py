import requests
from config import API_KEY

headers = {
    "x-apisports-key": API_KEY
}

def last_matches(team_id):

    url = f"https://v3.football.api-sports.io/fixtures"

    params = {
        "team": team_id,
        "last": 5
    }

    response = requests.get(url, headers=headers, params=params)

    return response.json()
