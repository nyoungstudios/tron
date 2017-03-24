
def findLocationHead(playerNum, grid_size, board_state):
    for i in range(0, grid_size):
        for j in range(0, grid_size):
            if playerNum == board_state[i][j]:
                return [i, j]
