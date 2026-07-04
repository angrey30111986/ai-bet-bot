import requests
from config import API_KEY

def get_matches():

    url = "https://v3.football.api-sports.io/fixtures?next=5"

    headers = {
        "x-apisports-key": API_KEY
    }

    response = requests.get(url, headers=headers)

    return response.json()
