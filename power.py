def power(stats):

    attack = stats["goals_for"]

    defense = stats["goals_against"]

    wins = stats["wins"]

    draws = stats["draws"]

    losses = stats["losses"]

    return attack * 3 - defense + wins * 5 + draws - losses * 2
