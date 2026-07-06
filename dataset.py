import requests
import pandas as pd
from config import API_KEY

headers = {
    "x-apisports-key": API_KEY
}

rows = []

for season in [2023, 2024, 2025]:
    print(f"Сезон {season}")

    response = requests.get(
        "https://v3.football.api-sports.io/fixtures",
        headers=headers,
        params={
            "league": 39,
            "season": season
        }
    )

    data = response.json()["response"]

    for match in data:

        rows.append({

            "home_goals": match["goals"]["home"],
            "away_goals": match["goals"]["away"],

            "result":
                1 if match["goals"]["home"] > match["goals"]["away"]
                else 0 if match["goals"]["home"] == match["goals"]["away"]
                else 2

        })

pd.DataFrame(rows).to_csv("matches.csv", index=False)

print("matches.csv створено")
