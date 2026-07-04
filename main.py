from analyzer import get_matches

data = get_matches()

for match in data["response"]:
    home = match["teams"]["home"]["name"]
    away = match["teams"]["away"]["name"]
    league = match["league"]["name"]

    print(f"{league}")
    print(f"{home} - {away}")
    print("----------------")
