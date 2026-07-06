from collections import defaultdict

history = defaultdict(list)

def add(team, result):

    history[team].append(result)

    if len(history[team]) > 5:
        history[team].pop(0)

def form(team):

    if team not in history:
        return 0

    return sum(history[team])
