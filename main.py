from GameManager import board as BD
 
board=BD.init_board()
#while(True):
     #while(True):
    
arr=BD.getAvailableMoves(board,11,23)
print(arr)