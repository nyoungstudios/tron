import math

def playerProb(playerNum, playerPos, otherPos, grid_size, board_state):
    #Find closest player
    closestPlayer = []
    minDistance = 100
    for element in otherPos:
        distance = math.sqrt(math.pow(element[0] - playerPos[0], 2) + math.pow(element[1] - playerPos[1], 2))
        if (distance < minDistance):
            closestPlayer = element

    #Look for walls and trails
    leftProb = rightProb = upProb = downProb = 0
    if playerPos[0] - 1 >= 0:
        if int(board_state[playerPos[0] - 1][playerPos[1]]) != 0:
            upProb -= 5
        if int(board_state[playerPos[0] - 1][playerPos[1]]) == playerNum:
            upProb -= 5
    else:
        upProb -= 5
    if playerPos[0] + 1 < grid_size:
        if int(board_state[playerPos[0] + 1][playerPos[1]]) != 0:
            downProb -= 5
        if int(board_state[playerPos[0] + 1][playerPos[1]]) == playerNum:
            downProb -= 5
    else:
        downProb -= 5
    if playerPos[1] - 1 >= 0:
        if int(board_state[playerPos[0]][playerPos[1] - 1]) != 0:
            leftProb -= 5
        if int(board_state[playerPos[0]][playerPos[1] - 1]) == playerNum:
            leftProb -= 5
    else:
        leftProb -= 5
    if playerPos[1] + 1 < grid_size:
        if int(board_state[playerPos[0]][playerPos[1] + 1]) != 0:
            rightProb -= 5
        if int(board_state[playerPos[0]][playerPos[1] + 1]) == playerNum:
            rightProb -= 5
    else:
        rightProb -= 5

    if closestPlayer[0] < playerPos[0]:
        upProb += 1
    elif closestPlayer[0] > playerPos[0]:
        downProb += 1
    if closestPlayer[1] > playerPos[1]:
        rightProb += 1
    elif closestPlayer[1] < playerPos[1]:
        leftProb += 1

    return [upProb, leftProb, rightProb, downProb]

