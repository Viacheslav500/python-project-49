from brain_games.cli import welcome_user


def run_game(game_func, task):
    user_name = welcome_user()
    print(task)
    count = 0
    while count != 3:
        answer, question = game_func()
        print(f'Question: {question}')
        user_answer = input('Your answer: ')
        if str(user_answer) == str(answer):
            print('Correct!')
            count += 1
        else:
            print(f"'{user_answer}' is wrong ;(. "
                  f"Correct answer was '{answer}'.\n"
                  f"Let's try again, {user_name}!"
                  )
            break
        if count == 3:
            print(f'Congratulations, {user_name}!')
