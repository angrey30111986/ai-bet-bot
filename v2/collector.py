from elo import get_elo
from fatigue import get_fatigue
from injuries import get_injuries
from cards import get_cards
from weather import get_weather


def collect_data(home_team, away_team, fixture_id):

    elo = get_elo(home_team, away_team)

    fatigue = get_fatigue(home_team, away_team)

    injuries = get_injuries(fixture_id)

    cards = get_cards(fixture_id)

    weather = get_weather(fixture_id)

    data = {}

    data.update(elo)
    data.update(fatigue)
    data.update(injuries)
    data.update(cards)
    data.update(weather)

    return data
