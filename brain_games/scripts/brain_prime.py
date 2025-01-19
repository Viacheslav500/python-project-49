from brain_games.cli import welcome_user
import random


user_name = welcome_user()
print('Answer "yes" if given number is prime. Otherwise answer "no".')
count = 0


def is_prime(number):
    if number <= 1:
        return False
    if number <= 3:
        return True
    if number % 2 == 0:
        return False
    for i in range(3, number // 2):
        if number % i == 0:
            return False
    return True


def make_answer(user_answer: str, right_answer: str):
    global count
    if right_answer == user_answer:
        print('Correct!')
        count += 1
    else:
        print(f"'{user_answer}' is wrong answer ;(."
              f"Correct answer was '{right_answer}'.\n"
              f"Let's try again, {user_name}!"
              )
        count = 0


def main():
    while count != 3:
        random_number = random.randrange(2, 100)
        print(f'Question: {random_number}')
        user_answer = input('Your answer: ')
        right_answer = 'yes' if is_prime(random_number) else 'no'
        make_answer(user_answer, right_answer)
    print(f'Congratulations, {user_name}!')


if __name__ == "__main__":
    main()
