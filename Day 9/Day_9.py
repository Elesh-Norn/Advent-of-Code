def game(player, last_marble):
    # Set the game
    global STACK, CURRENT_MARBLE, player_list, ACTIVE_PLAYER, SCORE, BEST_MARBLE
    STACK = [0]
    CURRENT_MARBLE = 1
    player_list = [x for x in range(1, player +1)]
    ACTIVE_PLAYER = 1
    SCORE = {}
    BEST_MARBLE = 0
    for player in player_list:
        SCORE[player] = 0

    while last_marble > BEST_MARBLE:
        turn()

    return SCORE

def player_change():
    global ACTIVE_PLAYER
    ACTIVE_PLAYER = player_list.pop(0)
    player_list.append(ACTIVE_PLAYER)


def place_marble():
    global CURRENT_MARBLE
    STACK.insert(0, STACK.pop(-1))
    STACK.insert(0, STACK.pop(-1))
    STACK.insert(-1, CURRENT_MARBLE)
    CURRENT_MARBLE += 1


def turn():
    global CURRENT_MARBLE, BEST_MARBLE
    player_change()
    if CURRENT_MARBLE % 23 == 0:
        # Score
        marble = CURRENT_MARBLE
        for X in range(0, 7):
            STACK.insert(-1, STACK.pop(0))
        removed = STACK.pop(-3)
        SCORE[ACTIVE_PLAYER] += marble + removed
        BEST_MARBLE = marble
        CURRENT_MARBLE += 1
        player_change()
        STACK.insert(-4, CURRENT_MARBLE)
        CURRENT_MARBLE += 1
    else:
        place_marble()

print(game(9, 23))