import requests
import pandas as pd
import time
from config import API_KEY

headers = {
    "x-apisports-key": API_KEY
}

# Ліги
leagues = [
    39,   # Англія
    140,  # Іспанія
    135,  # Італія
    78,   # Німеччина
    61,   # Франція
    94,   # Португалія
    88,   # Нідерланди
    203,  # Туреччина
    307,  # Саудівська Аравія
    71    # Бразилія
]

rows = []

for league in leagues:

    for season in [2022, 2023, 2024, 2025]:

        print(f"Ліга {league} Сезон {season}")

        r = requests.get(
            "https://v3.football.api-sports.io/fixtures",
            headers=headers,
            params={
                "league": league,
                "season": season
            }
        )

        data = r.json()["response"]

        for match in data:

            if match["goals"]["home"] is None:
                continue

            rows.append({

                "league": league,

                "season": season,

                "home": match["teams"]["home"]["name"],

                "away": match["teams"]["away"]["name"],

                "home_goals": match["goals"]["home"],

                "away_goals": match["goals"]["away"],

                "result":
                    1 if match["goals"]["home"] >
                    match["goals"]["away"]

                    else 0 if
                    match["goals"]["home"] ==
                    match["goals"]["away"]

                    else 2

            })

        time.sleep(1)

df = pd.DataFrame(rows)

df.to_csv("matches.csv", index=False)

print(df.head())

print(len(df))
