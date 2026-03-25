import random


def choose_difficulty() -> int:
    print("\n난이도를 선택하세요.")
    print("1. 쉬움 (1~50)")
    print("2. 보통 (1~100)")
    print("3. 어려움 (1~200)")

    while True:
        level = input("난이도 번호를 입력하세요: ")

        if level == "1":
            return 50
        if level == "2":
            return 100
        if level == "3":
            return 200

        print("1, 2, 3 중에서 입력해 주세요.")


def ask_replay() -> bool:
    while True:
        answer = input("다시 플레이할까요? (y/n): ").lower()

        if answer == "y":
            return True
        if answer == "n":
            return False

        print("y 또는 n만 입력해 주세요.")


def play_number_guess_game() -> None:
    print("=== 숫자 맞히기 게임 ===")

    while True:
        max_number = choose_difficulty()
        print(f"1부터 {max_number} 사이의 숫자를 맞혀 보세요!")

        answer = random.randint(1, max_number)
        attempts = 0

        while True:
            user_input = input("숫자를 입력하세요: ")

            if not user_input.isdigit():
                print("숫자만 입력해 주세요.")
                continue

            guess = int(user_input)

            if guess < 1 or guess > max_number:
                print(f"1부터 {max_number} 사이의 숫자를 입력해 주세요.")
                continue

            attempts += 1

            if guess < answer:
                print("UP! 더 큰 숫자입니다.")
            elif guess > answer:
                print("DOWN! 더 작은 숫자입니다.")
            else:
                print(f"정답입니다! 시도 횟수: {attempts}회")
                break

        if not ask_replay():
            print("게임을 종료합니다.")
            break


if __name__ == "__main__":
    play_number_guess_game()
