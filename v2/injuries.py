import requests

API_KEY = "03b997d33e6e88f7b1dc3e9f179d7f17"

headers = {
    "x-apisports-key": API_KEY
}


def get_injuries(fixture_id):

    url = "https://v3.football.api-sports.io/injuries"

    params = {
        "fixture": fixture_id
    }

    response = requests.get(
        url,
        headers=headers,
        params=params
    )

    if response.status_code != 200:
        print("API Error:", response.status_code)
        return []

    data = response.json()

    if "response" not in data:
        return []

    return data["response"]


if __name__ == "__main__":

    fixture_id = 1035039  # Для тесту заміни на потрібний ID матчу

    injuries = get_injuries(fixture_id)

    print("Кількість травм:", len(injuries))

    for player in injuries:
        print(player)
