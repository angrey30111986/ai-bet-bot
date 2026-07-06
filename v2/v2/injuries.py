import requests

API_KEY = "ТВІЙ_API_KEY"

headers = {
    "x-apisports-key": API_KEY
}

def get_injuries(fixture_id):
    url = f"https://v3.football.api-sports.io/injuries?fixture={fixture_id}"

    r = requests.get(url, headers=headers)

    if r.status_code != 200:
        return []

    return r.json()["response"]
