import requests
from config import API_KEY

headers = {
    "x-apisports-key": API_KEY
}


def get_matches(league, season):

    url = f"https://v3.football.api-sports.io/fixtures?league={league}&season={season}"

    r = requests.get(url, headers=headers)

    return r.json()["response"]


if __name__ == "__main__":

    leagues = [
        39,
        140,
        78,
        61,
        94,
        135,
        253,
        71,
        144,
        88
    ]

    seasons = [
        2022,
        2023,
        2024,
        2025
    ]

    total = 0

    for league in leagues:
        for season in seasons:

            print(f"Ліга {league} Сезон {season}")

            matches = get_matches(league, season)

            print("Матчів:", len(matches))

            total += len(matches)

    print()
    print("Всього матчів:", total)
