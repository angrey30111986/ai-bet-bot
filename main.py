from analyzer import get_matches

data = get_matches()

for match in data["response"][:5]:

    home = match["teams"]["home"]["name"]
    away = match["teams"]["away"]["name"]

    print(f"{home} - {away}")

    print("Прогноз: П1")
    print("Ймовірність: 72%")
    print("Тотал: Більше 2.5")
    print("-------------------")
