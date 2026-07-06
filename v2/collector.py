import requests
import pandas as pd
from config import API_KEY

headers = {
    "x-apisports-key": API_KEY
}

LEAGUES = [
    39,   # England
    140,  # Spain
    78,   # Germany
    61,   # France
    94,   # Portugal
    135,  # Italy
    253,  # MLS
    71,   # Brazil
    144,  # Belgium
    88    # Netherlands
]

SEASONS = [
    2022,
    2023,
    2024,
    2025
]

rows = []

for league in LEAGUES:

    for season in SEASONS:

        print(f"League {league} Season {season}")

        url = "https://v3.football.api-sports.io/fixtures"

        params = {
            "league": league,
            "season": season
        }

        response = requests.get(
            url,
            headers=headers,
            params=params
        )

        data = response.json()["response"]

        for match in data:

            if match["fixture"]["status"]["short"] != "FT":
                continue

            rows.append({

                "date": match["fixture"]["date"],

                "league": league,

                "season": season,

                "home_id": match["teams"]["home"]["id"],

                "away_id": match["teams"]["away"]["id"],

                "home_team": match["teams"]["home"]["name"],

                "away_team": match["teams"]["away"]["name"],

                "home_goals": match["goals"]["home"],

                "away_goals": match["goals"]["away"]

            })

df = pd.DataFrame(rows)

df.to_csv("matches.csv", index=False)

print("================================")

print("Matches saved:", len(df))

print(df.head())

print("================================")
