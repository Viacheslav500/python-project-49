import random
from brain_games.cli import welcome_user


def make_right_answer(number_a, number_b):
    while number_b:
        number_a, number_b = number_b, number_a % number_b
    return number_a


def main():
    count = 0
    user_name = welcome_user()
    print('Find the greatest common divisor of given numbers.')
    while count != 3:
        number_a = random.randrange(100)
        number_b = random.randrange(100)
        answer = make_right_answer(number_a, number_b)
        print(f'Question: {number_a} {number_b}')
        user_answer = int(input('Your answer: '))
        if answer == user_answer:
            print('Correct!')
            count += 1
        else:
            print(f"'{user_answer}' is wrong answer ;(."
                  f"Correct answer was '{answer}'.\n"
                  f"Let's try again, {user_name}!"
                  )
            break
    if count == 3:
        print(f'Congratulations, {user_name}!')


if __name__ == "__main__":
    main()
