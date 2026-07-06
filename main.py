from analyzer import get_matches
from predict import predict

data = get_matches()

for match in data["response"][:10]:

    home = match["teams"]["home"]["name"]
    away = match["teams"]["away"]["name"]

    hg = match["goals"]["home"]
    ag = match["goals"]["away"]

    home_form = 8
    away_form = 5

    result, chance = predict(home_form, away_form)

    print("-------------------------")
    print(home, "-", away)
    print("Прогноз:", result)
    print("Ймовірність:", str(chance) + "%")
