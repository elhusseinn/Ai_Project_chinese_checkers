from hashlib import new
from GameManager import board as BD
from PC_Move_Controller import controller as controller

board=BD.init_board()
newBoard = board.copy()
states = controller.generateStates(board)

for state in states:
    BD.printBoard(state)
    print ("/n")



