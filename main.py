from GameManager import board as BD
 
board=BD.init_board()
WinStatus=-1
#while(True):
     #while(True):
    
arr=BD.getAvailableMoves(board,8,12)
print(arr)