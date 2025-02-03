import random


def make_progression():
    step = random.randint(1, 11)
    start = random.randrange(1, 101)
    col = list()
    for _ in range(10):
        number = start
        col.append(str(number))
        start += step
    progression = col
    missing_index = random.randint(0, len(progression) - 1)
    right_answer = progression[missing_index]
    progression[missing_index] = '..'
    progression_str = ' '.join(progression)
    return right_answer, progression_str
