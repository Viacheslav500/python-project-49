import random 
from brain_games.cli import welcome_user
def main():
    name = welcome_user()
    print('Answer "yes" if the number is even, otherwise answer "no".')
    count = 0
    while count != 3:
        number = random.randrange(100)
        print(f'{"Question: "}{number}')
        answer = input('Your answer: ')
        if number % 2 == 0:
            if answer == 'yes':
                print('Correct!')
                count += 1
            if answer == 'no':
                print(f"'no' is wrong answer ;(. Correct answer was 'yes'. \n Let's try again, {user_name}!")
                if count > 0:
                    count = 0
        if number % 2 != 0:
            if answer == 'no':
                print('Correct!')
                count += 1
            if answer == 'yes':
                print(f"'yes' is wrong answer ;(. Correct answer was 'no'. \n Let's try again, {user_name}!")
                if count > 0:
                    count = 0
    print('Congrtulations, {user_name}')


if __name__ == "__main__":
    main()
