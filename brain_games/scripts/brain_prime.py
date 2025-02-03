from brain_games.games.prime import make_prime
from brain_games.engine import run_game


TASK = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def main():
    run_game(make_prime, TASK)


if __name__ == "__main__":
    main()
