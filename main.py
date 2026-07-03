from analyzer import analyze_match

home = "Реал Мадрид"
away = "Барселона"

result = analyze_match(home, away)

print("=== ПРОГНОЗ ===")
print(f"Матч: {home} - {away}")
print(f"Переможець: {result['winner']}")
print(f"Ймовірність: {result['confidence']}%")
print(f"Ставка: {result['prediction']}")
