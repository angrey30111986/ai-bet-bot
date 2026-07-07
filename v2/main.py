from predictor import predict_match

def main():
    print("=== AI BET BOT ===")

    home = input("Домашня команда: ")
    away = input("Гостьова команда: ")

    result = predict_match(home, away)

    print(result)

if __name__ == "__main__":
    main()
