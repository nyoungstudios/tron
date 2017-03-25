import numpy as math

def playerProb(playerPos, otherPos, grid_size, board_state):
    #Find closest player
    cPlayerNum = 0
    minDistance = 100
    for element in otherPos:
        distance = math.sqrt(math.square(element[0] - playerPos[0]) + math.square(element[1] - playerPos[1]))
        if (distance < minDistance):
            cPlayerNum = board_state[element[0]][element[1]]

    #Look for walls and trails
    leftProb = rightProb = upProb = downProb = 0
    if playerPos[0] - 1 >= 0:
        if board_state[playerPos[]]
    else:



def moveProbability(myPosition, otherPosition, grid_size, board_state):
    leftProb = rightProb = upProb = downProb = 0
