import requests
from config import API_KEY

def get_team_last_matches(team_id):

    url = f"https://v3.football.api-sports.io/fixtures?team={team_id}&last=5"

    headers = {
        "x-apisports-key": API_KEY
    }

    response = requests.get(url, headers=headers)
    return response.json()
