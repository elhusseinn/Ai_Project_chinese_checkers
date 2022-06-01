from GameManager import board as BD
 
board=BD.init_board()
#while(True):
     #while(True):
    
arr=BD.getAvailableMoves(board,14,14)
print(arr)