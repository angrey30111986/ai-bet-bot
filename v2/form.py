from collections import defaultdict

history = defaultdict(list)


def get_form(team):

    games = history[team][-5:]

    if not games:
        return 0.5

    return sum(games) / len(games)


def update_form(home, away, result):

    if result == 0:

        history[home].append(1)
        history[away].append(0)

    elif result == 1:

        history[home].append(0.5)
        history[away].append(0.5)

    else:

        history[home].append(0)
        history[away].append(1)
