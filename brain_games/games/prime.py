import random


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


def make_prime():
    random_number = random.randrange(2, 100)
    right_answer = 'yes' if is_prime(random_number) else 'no'
    return right_answer, random_number
