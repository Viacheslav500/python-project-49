from brain_games.cli import welcome_user
import random


def make_the_operation(num_a: int, num_b: int, sign: str):
    if sign == '+':
        return num_a + num_b
    if sign == '-':
        return num_a - num_b
    if sign == '*':
        return num_a * num_b


def main():
    user_name = welcome_user()
    print('What is the result of the expression?')
    count = 0
    while count != 3:
        number_a = random.randrange(100)
        number_b = random.randrange(100)
        operator = random.choice(['*', '-', '+'])
        print(f'Question: {number_a} {operator} {number_b}')
        result = make_the_operation(number_a, number_b, operator)
        user_answer = int(input('Your answer: '))
        if result == user_answer:
            print('Correct!')
            count += 1
        else:
            print(
                f"'{user_answer}' is wrong answer ;(."
                f"Correct answer was '{result}'.\n"
                f"Let's try again, {user_name}!"
            )
            break
    if count == 3:
        print(f'Congratulations, {user_name}!')


if __name__ == "__main__":
    main()
