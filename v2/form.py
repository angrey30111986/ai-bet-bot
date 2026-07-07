from collections import defaultdict

history = defaultdict(list)


def add_result(team, points):

    history[team].append(points)

    if len(history[team]) > 5:
        history[team].pop(0)


def get_form(team):

    games = history[team]

    if not games:
        return 0

    return sum(games) / len(games)
