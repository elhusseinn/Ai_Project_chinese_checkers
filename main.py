from hashlib import new
from GameManager import board as BD
from PC_Move_Controller import controller as controller

board=BD.init_board()
# board[3][11] = 0
# board[4][10] = 1
# board[14][14] = 0
# board[12][16] = 2
# board[3][9] = 0
# board[5][11] = 1
# board[14][10] = 0
# board[12][12] = 2
# board[3][9] = 0
# board[5][11] = 1

# BD.printBoard(board)
for i in range (15):
    BD.printBoard(controller.PC_Move(board, 3))

# print(controller.eclidiean_distance([3,9],[16,12]))




