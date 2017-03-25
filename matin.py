import math

def playerProb(playerPos, otherPos, grid_size, board_state):
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
        if board_state[playerPos[]]
    else:
        upProb -= 500
    if playerPos[0] + 1 < grid_size:
    else:
        downProb -=  500
    if playerPos[1] - 1 < 0:
    else:
        leftProb -= 500
    if playerPos[1] + 1


def moveProbability(myPosition, otherPosition, grid_size, board_state):
    leftProb = rightProb = upProb = downProb = 0
