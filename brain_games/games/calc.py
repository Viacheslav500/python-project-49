import random


def make_the_result(num_a: int, num_b: int, sign: str):
    if sign == '+':
        return num_a + num_b
    if sign == '-':
        return num_a - num_b
    if sign == '*':
        return num_a * num_b


def make_calc():
    number_a = random.randrange(100)
    number_b = random.randrange(100)
    operator = random.choice(['*', '-', '+'])
    question = f'{number_a} {operator} {number_b}'
    result = make_the_result(number_a, number_b, operator)
    return result, question
