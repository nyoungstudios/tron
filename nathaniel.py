
def findLocationHead(playerNum, grid_size, board_state):
    i = -1
    j = -1
    for row in board_state:
        i += 1
        for cell in row:
            j += 1
            if playerNum == cell:
                return [i, j]
        j = -1
