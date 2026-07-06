from collector import collect_data


def predict(home_team, away_team, fixture_id):

    data = collect_data(
        home_team,
        away_team,
        fixture_id
    )

    home = 50

    if data["elo_diff"] > 100:
        home += 10

    if data["home_rest_days"] > data["away_rest_days"]:
        home += 5

    if data["home_injuries"] < data["away_injuries"]:
        home += 5

    if data["temperature"] > 30:
        home -= 2

    if data["wind"] > 25:
        home -= 2

    draw = 100 - home
    away = 100 - home - draw // 2

    return {
        "home": round(home),
        "draw": round(draw / 2),
        "away": round(away)
    }
