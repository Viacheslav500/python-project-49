import random


def make_even():
    number = random.randrange(100)
    right_answer = ''
    if number % 2 == 0:
        right_answer = 'yes'
    else:
        right_answer = 'no'
    return right_answer, number
