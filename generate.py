import random

def generate_random_number(length = 4):
    all_digits = list(range(10))
    random.shuffle(all_digits)
    random_integer = ''.join(map(str, all_digits[:length]))

    return random_integer