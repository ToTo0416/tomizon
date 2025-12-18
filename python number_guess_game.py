import random

def number_guess_game():
    print("=== 数当てゲーム ===")
    print("1から100までの数字を当ててください！")

    answer = random.randint(1, 100)
    attempts = 0

    while True:
        try:
            guess = int(input("予想した数字を入力: "))
        except ValueError:
            print("数字を入力してください。")
            continue

        attempts += 1

        if guess < answer:
            print("もっと大きいです")
        elif guess > answer:
            print("もっと小さいです")
        else:
            print(f"正解！ {attempts}回で当てました！")
            break

if __name__ == "__main__":
    number_guess_game()
