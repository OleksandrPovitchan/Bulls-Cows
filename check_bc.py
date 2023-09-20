def check_for_bulls_and_cows(first_player_turn_, second_player_turn_):
    bulls_ = 0 #exactly the same
    cows_ = 0 #right digit but incorrect position

    for i in range(len(first_player_turn_)):
        if first_player_turn_[i] == second_player_turn_[i]:
            bulls_ += 1

    for i in range(len(first_player_turn_)):
        for j in range(len(first_player_turn_)):
            if first_player_turn_[i] == second_player_turn_[j]:
                cows_ += 1

    cows_ -= bulls_

    return bulls_, cows_