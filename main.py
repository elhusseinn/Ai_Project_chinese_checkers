from GameManager import board as BD
from PC_Move_Controller import controller as controller
 
board=BD.init_board()


print(controller.generateSearchSpace(board))