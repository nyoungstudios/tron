from tron_connection import TronSocket
import matin as m
import nathaniel as n

secret = "UUCRU1490393876171" #TODO: SET SECRET HERE

'''
Print the board
@param {double array} board_state: A matrix representing the state of the board
'''
def print_board(board_state):
  for row in board_state:
    for cell in row:
      print(cell,end=' ')
    print("")

'''
 Return the direction you want to move your bike in
 @param  {int} grid_size:            The length of one side of the square grid
 @param  {double array} board_state: A 2D matrix of ints representing the state of the board
 @param  {int} my_player_number:     The number which represens your player on the board
 @param  {int} total_player_count:   The amount of players in this gane
 @return {String}                    The move to be played ("UP", "DOWN", "LEFT", or "RIGHT")
'''
def select_move(grid_size, board_state, my_player_number, total_player_count):

  #=================================================#
  # TODO: YOUR CODE HERE                            #
  # TODO: Return "UP", "DOWN", "LEFT", or "RIGHT"   #
  #=================================================#




  currentLocationList = []
  for x in range(int(total_player_count)):
    currentPlayerNum = int(x + 1)
    #print(currentPlayerNum)
    location = n.findLocationHead(str(currentPlayerNum), grid_size, board_state)
    currentLocationList.insert(currentPlayerNum, location)
    #print("this is the pos " + str(currentLocationList[currentPlayerNum-1]) + " This is x:")

  ourCurrentLocation = currentLocationList[int(my_player_number) - 1]
  otherLocation = currentLocationList
  otherLocation.remove(ourCurrentLocation)

  probList = m.playerProb(int(my_player_number), ourCurrentLocation, otherLocation, grid_size, board_state)
  print(probList)

  currentVal = 0
  largestVal = 0
  largestIndex = 0
  i = 0
  for y in probList:
    currentVal = y
    if i == 0:
      largestVal = currentVal
      largestIndex = i
    elif currentVal > largestVal:
      largestVal = currentVal
      largestIndex = i

    i+=1


  print_board(board_state)  # Print board for debugging
  print("")

  if largestIndex == 0:
    return "UP"
  elif largestIndex == 1:
    return "LEFT"
  elif largestIndex == 2:
    return "RIGHT"
  elif largestIndex == 3:
    return "DOWN"








  # Return "UP", "LEFT", "LEFT", or "RIGHT"
  return "UP"



#DON'T TOUCH BELOW
socket_connection = TronSocket(select_move, secret)
#DON'T TOUCH ABOVE
