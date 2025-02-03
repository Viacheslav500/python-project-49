from brain_games.games.progression import make_progression
from brain_games.engine import run_game


TASK = 'What number is missing in the progression?'


def main():
    run_game(make_progression, TASK)


if __name__ == "__main__":
    main()
