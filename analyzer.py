import requests

def analyze_match(home, away):
    url = "https://www.thesportsdb.com/api/v1/json/3/searchteams.php"

    home_data = requests.get(url, params={"t": home}).json()
    away_data = requests.get(url, params={"t": away}).json()

    home_found = home_data.get("teams")
    away_found = away_data.get("teams")

    if not home_found or not away_found:
        return {
            "winner": "Невідомо",
            "confidence": 0,
            "prediction": "Немає даних"
        }

    return {
        "winner": home,
        "confidence": 70,
        "prediction": "П1"
    }
