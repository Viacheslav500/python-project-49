from brain_games.engine import run_game
from brain_games.games.even import make_even


TASK = 'Answer "yes" if the number is even, otherwise answer "no".'


def main():
    run_game(make_even, TASK)


if __name__ == "__main__":
    main()
