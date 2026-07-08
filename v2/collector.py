from elo import get_elo
from fatigue import get_fatigue
from injuries import get_injuries
from cards import get_cards
from weather import get_weather


def collect_data(home_team, away_team, fixture_id=None, fixture=None):

    data = {}

    # Elo
    data.update(get_elo(home_team, away_team))

    # Відпочинок
    data.update(get_fatigue(home_team, away_team, fixture))

    # Значення за замовчуванням
    data.update({
        "home_injuries": 0,
        "away_injuries": 0,
        "home_yellow": 0,
        "away_yellow": 0,
        "home_red": 0,
        "away_red": 0,
        "temperature": None,
        "weather": None,
        "wind": None,
        "humidity": None
    })

    if not fixture_id:
        return data

    # Травми
    injuries = get_injuries(fixture_id)

    if isinstance(injuries, list):

        for player in injuries:

            team = player.get("team", {}).get("name", "")

            if team == home_team:
                data["home_injuries"] += 1

            elif team == away_team:
                data["away_injuries"] += 1

    # Картки
    cards = get_cards(fixture_id)

    if isinstance(cards, dict):
        data.update(cards)

    # Погода
    weather = get_weather(fixture_id)

    if isinstance(weather, dict):
        data.update(weather)

    return data
