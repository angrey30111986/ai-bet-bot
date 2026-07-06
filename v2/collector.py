import requests
import pandas as pd
from config import API_KEY

headers = {
    "x-apisports-key": API_KEY
}

LEAGUES = [39, 140, 78, 61, 94, 135, 253, 71, 144, 88]
SEASONS = [2022, 2023, 2024, 2025]

rows = []

for league in LEAGUES:
    for season in SEASONS:

        print(f"League {league} Season {season}")

        url = f"https://v3.football.api-sports.io/fixtures?league={league}&season={season}"

        data = requests.get(url, headers=headers).json()["response"]

        for match in data:

            if match["fixture"]["status"]["short"] != "FT":
                continue

            home = match["teams"]["home"]["name"]
            away = match["teams"]["away"]["name"]

            hg = match["goals"]["home"]
            ag = match["goals"]["away"]

            rows.append({
                "home": home,
                "away": away,
                "home_goals": hg,
                "away_goals": ag
            })

df = pd.DataFrame(rows)

df.to_csv("matches.csv", index=False)

print("Saved", len(df), "matches")
