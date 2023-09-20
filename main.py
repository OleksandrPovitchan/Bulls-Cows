import sys

from check_bc import check_for_bulls_and_cows
from generate import generate_random_number

first_player_turn = generate_random_number()
bulls = 0
print('The number has been created!')

attempt = 1

while bulls < 4:
    print('Please, enter your guess now')
    second_player_turn = input()

    bulls, cows = check_for_bulls_and_cows(first_player_turn, second_player_turn)
    print(f'ATTEMPT #{attempt} || Your number: {second_player_turn} || BULLS: {bulls} || COWS {cows}')

    attempt += 1

print(f'CONGRATULATIONS! (only {attempt-1} attempts)')

sys.exit()