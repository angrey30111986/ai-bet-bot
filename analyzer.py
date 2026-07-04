import requests
from config import API_KEY

def get_matches():

    url = "https://v3.football.api-sports.io/fixtures?date=2026-07-04"
    headers = {
        "x-apisports-key": API_KEY
    }

    response = requests.get(url, headers=headers)

    return response.json()
