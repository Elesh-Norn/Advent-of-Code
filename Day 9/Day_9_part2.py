from collections import deque
def game(player, last_marble):
    # Set the game
    global STACK, CURRENT_MARBLE, player_list, ACTIVE_PLAYER, SCORE
    STACK = deque()
    STACK.append(0)
    CURRENT_MARBLE = 1
    player_list = [x for x in range(1, player +1)]
    ACTIVE_PLAYER = 1
    SCORE = {}

    for player in player_list:
        SCORE[player] = 0

    while last_marble > CURRENT_MARBLE:
        turn()
        if CURRENT_MARBLE % 71700 == 0:
            print(CURRENT_MARBLE/71700)
    return SCORE

def player_change():
    global ACTIVE_PLAYER
    ACTIVE_PLAYER = player_list.pop(0)
    player_list.append(ACTIVE_PLAYER)

def place_marble():
    global CURRENT_MARBLE

    STACK.rotate(2)
    STACK.append(CURRENT_MARBLE)
    CURRENT_MARBLE += 1


def turn():
    global CURRENT_MARBLE
    player_change()
    if CURRENT_MARBLE % 23 == 0:
        # Score
        STACK.rotate(-7)
        SCORE[ACTIVE_PLAYER] += CURRENT_MARBLE + STACK.pop()
        CURRENT_MARBLE += 1
        player_change()

    place_marble()

answer = game(405, 71700*100)

print(max(zip(answer.values(), answer.keys())))