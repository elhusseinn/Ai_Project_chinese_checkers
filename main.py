from hashlib import new
import sys
from GameManager import board as BD
from PC_Move_Controller import controller as controller
import sys
sys.setrecursionlimit(7000)
board=BD.init_board()

for i in range(15):
    BD.printBoard(controller.PC_Move(board, 3))
    print(controller.calculate_heuristic(board))

# print(controller.eclidiean_distance([3,9],[16,12]))






