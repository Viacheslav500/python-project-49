from brain_games.games.calc import make_calc
from brain_games.engine import run_game


QUESTION = 'What is the result of the expression?'


def main():
    run_game(make_calc, QUESTION)


if __name__ == "__main__":
    main()
