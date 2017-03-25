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
        if board_state[playerPos[0] - 1][playerPos[1]] != 0:
            upProb -= 500
    else:
        upProb -= 500
    if playerPos[0] + 1 < grid_size:
        if board_state[playerPos[0] + 1][playerPos[1]] != 0:
            downProb -= 500
    else:
        downProb -=  500
    if playerPos[1] - 1 >= 0:
        if board_state[playerPos[0]][playerPos[1] - 1] != 0:
            leftProb -= 500
    else:
        leftProb -= 500
    if playerPos[1] + 1 < grid_size:
        if board_state[playerPos[0]][playerPos[1] + 1] != 0:
            rightProb -= 500
    else:
        rightProb -= 500



#def moveProbability(myPosition, otherPosition, grid_size, board_state):
#    leftProb = rightProb = upProb = downProb = 0
