from brain_games.games.gcd import make_gcd
from brain_games.engine import run_game


TASK = 'Find the greatest common divisor of given numbers.'


def main():
    run_game(make_gcd, TASK)


if __name__ == "__main__":
    main()
