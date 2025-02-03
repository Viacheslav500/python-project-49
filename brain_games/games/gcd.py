import random


def make_right_answer(number_a, number_b):
    while number_b:
        number_a, number_b = number_b, number_a % number_b
    return number_a


def make_gcd():
    number_a = random.randrange(100)
    number_b = random.randrange(100)
    answer = make_right_answer(number_a, number_b)
    question = f'{number_a} {number_b}'
    return answer, question
