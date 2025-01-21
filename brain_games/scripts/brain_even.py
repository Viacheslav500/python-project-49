import random
from brain_games.cli import welcome_user


def make_answer(num: int):
    if num % 2 == 0:
        return 'yes'
    else:
        return 'no'


def main():
    user_name = welcome_user()
    print('Answer "yes" if the number is even, otherwise answer "no".')
    count = 0
    while count != 3:
        number = random.randrange(100)
        print(f'{"Question: "}{number}')
        answer = input('Your answer: ')
        if answer == make_answer(number):
            print('Correct!')
            count += 1
        else:
            print(f"'{answer}' is wrong answer ;(."
                  f"Correct answer was '{make_answer(number)}'.\n"
                  f"Let's try again, {user_name}!"
                  )
            count = 0
            break
    print(f'Congratulations, {user_name}!')


if __name__ == "__main__":
    main()
