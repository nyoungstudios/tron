
def findLocationHead(playerNum, grid_size, board_state):
    for row in board_state:
        for cell in row:
            if playerNum == cell:
                return 1

