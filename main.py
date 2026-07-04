from analyzer import get_matches

data = get_matches()

for match in data["response"]:

    home = match["teams"]["home"]["name"]
    away = match["teams"]["away"]["name"]

    hg = match["goals"]["home"]
    ag = match["goals"]["away"]

    print("---------------------")
    print(home, "-", away)
    print("Рахунок:", hg, ":", ag)

    if hg is not None and ag is not None:

        if hg > ag:
            print("Лідирує домашня команда")

        elif ag > hg:
            print("Лідирує гості")

        else:
            print("Нічия")
