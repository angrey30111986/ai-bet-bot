import requests
from config import API_KEY

BASE_URL = "https://v3.football.api-sports.io"

HEADERS = {
    "x-apisports-key": API_KEY
}


def test_endpoint(name, endpoint, params=None):

    print("=" * 60)
    print("Перевірка:", name)

    try:

        response = requests.get(
            BASE_URL + endpoint,
            headers=HEADERS,
            params=params,
            timeout=20
        )

        print("HTTP:", response.status_code)

        if response.status_code != 200:
            print(response.text[:300])
            return

        data = response.json()

        print("Results:", data.get("results"))

        if data.get("errors"):
            print("Errors:", data["errors"])

        if data.get("response"):
            print("OK")
        else:
            print("Порожня відповідь")

    except Exception as e:
        print("ERROR:", e)


if __name__ == "__main__":

    print("\nAPI TEST\n")

    test_endpoint(
        "Fixtures",
        "/fixtures",
        {
            "league": 39,
            "season": 2025
        }
    )

    test_endpoint(
        "Standings",
        "/standings",
        {
            "league": 39,
            "season": 2025
        }
    )

    test_endpoint(
        "Lineups",
        "/fixtures/lineups",
        {
            "fixture": 1035038
        }
    )

    test_endpoint(
        "Injuries",
        "/injuries",
        {
            "fixture": 1035038
        }
    )

    test_endpoint(
        "Odds",
        "/odds",
        {
            "fixture": 1035038
        }
    )

    test_endpoint(
        "Statistics",
        "/fixtures/statistics",
        {
            "fixture": 1035038
        }
    )
