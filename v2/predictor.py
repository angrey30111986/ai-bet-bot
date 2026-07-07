from collector import collect_data


def predict(home_team, away_team, fixture_id=None):
    data = collect_data(home_team, away_team, fixture_id)

    home = 50

    if data.get("elo_diff", 0) > 100:
        home += 10

    if data.get("home_rest_days", 0) > data.get("away_rest_days", 0):
        home += 5

    if data.get("home_injuries", 0) < data.get("away_injuries", 0):
        home += 5

    if data.get("temperature") is not None:
        if data["temperature"] > 30:
            home -= 2

    if data.get("wind") is not None:
        if data["wind"] > 25:
            home -= 2

    if home > 90:
        home = 90

    if home < 5:
        home = 5

    draw = 25

    away = 100 - home - draw

    return {
        "home": home,
        "draw": draw,
        "away": away
    }
