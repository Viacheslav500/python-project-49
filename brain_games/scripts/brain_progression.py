import random
from brain_games.cli import welcome_user


def main():
    step = random.randint(1, 11)
    start = random.randrange(1, 101)
    count = 0
    user_name = welcome_user()
    print('What number is missing in the progression?')
    while count != 3:
        col = list()
        for _ in range(10):
            number = start
            col.append(number)
            start += step
        progression = sorted(col)
        missing_index = random.randint(0, len(progression) - 1)
        right_answer = progression[missing_index]
        progression[missing_index] = '..'
        print(*progression)
        user_answer = int(input('Your answer: '))
        if user_answer == right_answer:
            print('Correct!')
            count += 1
            step = random.randint(1, 11)
        else:
            print(f"'{user_answer}' is wrong answer ;(."
                  f"Correct answer was '{right_answer}'.\n"
                  f"Let's try again, {user_name}!"
                  )
            break
    if count == 3:
        print(f'Congratulations, {user_name}!')


if __name__ == "__main__":
    main()
