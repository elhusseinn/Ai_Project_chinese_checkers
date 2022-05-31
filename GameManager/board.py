'''
1.represent board using 2D array coordinate system (with some of tree representation)
2.initialize the board with the appropriate position (1,2,3: for Player, 4,5,6: for PC, 0: for empty place to be played on, -1: for inaccessable index)
'''
from unittest import skip
import numpy


def init_board():
    board = numpy.full((17, 25), -1)

# Green is 1   To Human
    board[0][12] = 1
    board[1][11] = 1
    board[1][13] = 1
    board[2][10] = 1
    board[2][12] = 1
    board[2][14] = 1
    board[3][9] = 1
    board[3][11] = 1
    board[3][13] = 1
    board[3][15] = 1

# Yellow is 2

    board[4][18] = 2
    board[4][20] = 2
    board[4][22] = 2
    board[4][24] = 2
    board[5][19] = 2
    board[5][21] = 2
    board[5][23] = 2
    board[6][20] = 2
    board[6][22] = 2
    board[7][21] = 2


# Orange is 3

    board[9][21] = 3
    board[10][20] = 3
    board[10][22] = 3
    board[11][19] = 3
    board[11][21] = 3
    board[11][23] = 3
    board[12][18] = 3
    board[12][20] = 3
    board[12][22] = 3
    board[12][24] = 3


# Red is 4 To PC

    board[13][9] = 4
    board[13][11] = 4
    board[13][13] = 4
    board[13][15] = 4
    board[14][10] = 4
    board[14][12] = 4
    board[14][14] = 4
    board[15][11] = 4
    board[15][13] = 4
    board[16][12] = 4

# Purple is 5
    board[9][3] = 5
    board[10][2] = 5
    board[10][4] = 5
    board[11][1] = 5
    board[11][3] = 5
    board[11][5] = 5
    board[12][0] = 5
    board[12][2] = 5
    board[12][4] = 5
    board[12][6] = 5


# Blue is 6

    board[4][0] = 6
    board[4][2] = 6
    board[4][4] = 6
    board[4][6] = 6
    board[5][1] = 6
    board[5][3] = 6
    board[5][5] = 6
    board[6][2] = 6
    board[6][4] = 6
    board[7][3] = 6


# play ground space initial is 0


# level 4
    board[4][8] = 0
    board[4][10] = 0
    board[4][12] = 0
    board[4][14] = 0
    board[4][16] = 0
# level 5
    board[5][7] = 0
    board[5][9] = 0
    board[5][11] = 1
    board[5][13] = 1
    board[5][15] = 0
    board[5][17] = 0
# level 6
    board[6][6] = 0
    board[6][8] = 0
    board[6][10] = 0
    board[6][12] = 0
    board[6][14] = 0
    board[6][16] = 0
    board[6][18] = 0
# level 7
    board[7][5] = 0
    board[7][7] = 0
    board[7][9] = 0
    board[7][11] = 0
    board[7][13] = 1
    board[7][15] = 0
    board[7][17] = 0
    board[7][19] = 0
# level 8
    board[8][4] = 0
    board[8][6] = 0
    board[8][8] = 0
    board[8][10] = 0
    board[8][12] = 1
    board[8][14] = 0
    board[8][16] = 0
    board[8][18] = 0
    board[8][20] = 0
# level 9
    board[9][5] = 0
    board[9][7] = 0
    board[9][9] = 0
    board[9][11] = 0
    board[9][13] = 0
    board[9][15] = 0
    board[9][17] = 0
    board[9][19] = 0
# level 10
    board[10][6] = 0
    board[10][8] = 0
    board[10][10] = 0
    board[10][12] = 0
    board[10][14] = 0
    board[10][16] = 0
    board[10][18] = 0
# level 11

    board[11][7] = 0
    board[11][9] = 0
    board[11][11] = 0
    board[11][13] = 0
    board[11][15] = 0
    board[11][17] = 0

# level 12
    board[12][8] = 0
    board[12][10] = 0
    board[12][12] = 0
    board[12][14] = 0
    board[12][16] = 0

    return board


#if human wins retrun 1 >>>>> if pc wins return 0 <<<<< if none win return -1  
def checkWin(board):
    # if all (1)green colors is on the other side then Human win
    if board[13][9] == 1 and board[13][11] == 1 and board[13][13] == 1 and board[13][15] == 1 and board[14][10] == 1 and board[14][12] == 1 and board[14][14] == 1 and board[15][11] == 1 and board[15][13] == 1 and board[16][12] == 1:

      return 1
    # if all (4)Red colors is on the other side then Pc win
    elif board[0][12] == 4 and board[1][11] == 4 and board[1][13] == 4 and board[2][10] == 4 and board[2][12] == 4 and board[2][14] == 4 and board[3][9] == 4 and board[3][11] == 4 and board[3][13] == 4 and board[3][15] == 4:

        return 0

    else :
        return -1

#checkWin(1)

def getJumpMoves(board,backlevel,backindex,level,index):
    arrOfMoves=[]

    #TopRight
    newLevel=level-1
    newIndex=index+1
    if newLevel==backlevel and newIndex==backindex :
        skip
    elif board[newLevel][newIndex]==1 or board[newLevel][newIndex]==4 :
        newLevel=newLevel-1
        newIndex=newIndex+1 #get the topRight of TopRight
        if board[newLevel][newIndex]==0:
           arrOfMoves.append([newLevel,newIndex])
           newArrOfMoves=getJumpMoves(board,newLevel+1,newIndex-1,newLevel,newIndex)
           arrOfMoves.extend(newArrOfMoves)

    
    #Right
    newLevel=level
    newIndex=index+2
    if newLevel==backlevel and newIndex==backindex :
            skip
    elif board[newLevel][newIndex]==1 or board[newLevel][newIndex]==4 :    
         newLevel=newLevel
         newIndex=newIndex+2 #get the Right of Right
         if board[newLevel][newIndex]==0:
              arrOfMoves.append([newLevel,newIndex])
              newArrOfMoves=getJumpMoves(board,newLevel,newIndex-2,newLevel,newIndex)
              arrOfMoves.extend(newArrOfMoves)



    #DownRight
    newLevel=level+1
    newIndex=index+1
    if newLevel==backlevel and newIndex==backindex :
            skip
    elif board[newLevel][newIndex]==1 or board[newLevel][newIndex]==4 : 
         newLevel=newLevel+1
         newIndex=newIndex+1 #get the DownRight of DownRight
         if board[newLevel][newIndex]==0:
              arrOfMoves.append([newLevel,newIndex])
              newArrOfMoves=getJumpMoves(board,newLevel-1,newIndex-1,newLevel,newIndex)
              arrOfMoves.extend(newArrOfMoves)



    #TopLeft
    newLevel=level-1
    newIndex=index-1
    if newLevel==backlevel and newIndex==backindex :
            skip
    elif board[newLevel][newIndex]==1 or board[newLevel][newIndex]==4 : 
         n#get the TopLeft of TopLeftewLevel=newLevel-1
         newIndex=newIndex-1 
         if board[newLevel][newIndex]==0:
              arrOfMoves.append([newLevel,newIndex])
              newArrOfMoves=getJumpMoves(board,newLevel+1,newIndex+1,newLevel,newIndex)
              arrOfMoves.extend(newArrOfMoves)



    #Left
    newLevel=level
    newIndex=index-2
    if newLevel==backlevel and newIndex==backindex :
            skip
    elif board[newLevel][newIndex]==1 or board[newLevel][newIndex]==4 : 
         newLevel=newLevel
         newIndex=newIndex-2 #get the Left of Left
         if board[newLevel][newIndex]==0:
              arrOfMoves.append([newLevel,newIndex])
              newArrOfMoves=getJumpMoves(board,newLevel,newIndex+2,newLevel,newIndex)
              arrOfMoves.extend(newArrOfMoves)


    #DownLeft
    newLevel=level+1
    newIndex=index-1
    if newLevel==backlevel and newIndex==backindex :
        skip 
    elif board[newLevel][newIndex]==1 or board[newLevel][newIndex]==4 : 
           newLevel=newLevel+1
           newIndex=newIndex-1 #get the DownLeft of DownLeft
           if board[newLevel][newIndex]==0:
              arrOfMoves.append([newLevel,newIndex])
              newArrOfMoves=getJumpMoves(board,newLevel-1,newIndex+1,newLevel,newIndex)
              arrOfMoves.extend(newArrOfMoves) 


    return arrOfMoves

def getAvailableMoves(board,level,index):
    
    arrOfMoves=[]
    #TopRight
    newLevel=level-1
    newIndex=index+1
    if board[newLevel][newIndex]==0:
        arrOfMoves.append([newLevel,newIndex])
    elif board[newLevel][newIndex]==1 or board[newLevel][newIndex]==4 :#check top right if have value
        newLevel=newLevel-1
        newIndex=newIndex+1 #get the topRight of TopRight
        if board[newLevel][newIndex]==0:
           arrOfMoves.append([newLevel,newIndex])
           newArrOfMoves=getJumpMoves(board,newLevel+1,newIndex-1,newLevel,newIndex)
           arrOfMoves.extend(newArrOfMoves)
    
    #Right
    newLevel=level
    newIndex=index+2
    if board[newLevel][newIndex]==0:
        arrOfMoves.append([newLevel,newIndex])
    elif board[newLevel][newIndex]==1 or board[newLevel][newIndex]==4 :    
         newLevel=newLevel
         newIndex=newIndex+2 #get the Right of Right
         if board[newLevel][newIndex]==0:
              arrOfMoves.append([newLevel,newIndex])
              newArrOfMoves=getJumpMoves(board,newLevel,newIndex-2,newLevel,newIndex)
              arrOfMoves.extend(newArrOfMoves)



    #DownRight
    newLevel=level+1
    newIndex=index+1

    if board[newLevel][newIndex]==0:
        arrOfMoves.append([newLevel,newIndex])
    elif board[newLevel][newIndex]==1 or board[newLevel][newIndex]==4 : 
         newLevel=newLevel+1
         newIndex=newIndex+1 #get the DownRight of DownRight
         if board[newLevel][newIndex]==0:
              arrOfMoves.append([newLevel,newIndex])
              newArrOfMoves=getJumpMoves(board,newLevel-1,newIndex-1,newLevel,newIndex)
              arrOfMoves.extend(newArrOfMoves)








    #TopLeft
    newLevel=level-1
    newIndex=index-1
    if board[newLevel][newIndex]==0:
        arrOfMoves.append([newLevel,newIndex])
    elif board[newLevel][newIndex]==1 or board[newLevel][newIndex]==4 : 
         newLevel=newLevel-1
         newIndex=newIndex-1 #get the TopLeft of TopLeft
         if board[newLevel][newIndex]==0:
              arrOfMoves.append([newLevel,newIndex])
              newArrOfMoves=getJumpMoves(board,newLevel+1,newIndex+1,newLevel,newIndex)
              arrOfMoves.extend(newArrOfMoves)




    #Left
    newLevel=level
    newIndex=index-2
    if board[newLevel][newIndex]==0:
        arrOfMoves.append([newLevel,newIndex])
    elif board[newLevel][newIndex]==1 or board[newLevel][newIndex]==4 : 
         newLevel=newLevel
         newIndex=newIndex-2 #get the Left of Left
         if board[newLevel][newIndex]==0:
              arrOfMoves.append([newLevel,newIndex])
              newArrOfMoves=getJumpMoves(board,newLevel,newIndex+2,newLevel,newIndex)
              arrOfMoves.extend(newArrOfMoves)





    #DownLeft
    newLevel=level+1
    newIndex=index-1
    if board[newLevel][newIndex]==0:
        arrOfMoves.append([newLevel,newIndex])
    elif board[newLevel][newIndex]==1 or board[newLevel][newIndex]==4 : 
           newLevel=newLevel+1
           newIndex=newIndex-1 #get the DownLeft of DownLeft
           if board[newLevel][newIndex]==0:
              arrOfMoves.append([newLevel,newIndex])
              newArrOfMoves=getJumpMoves(board,newLevel-1,newIndex+1,newLevel,newIndex)
              arrOfMoves.extend(newArrOfMoves) 

    return arrOfMoves
