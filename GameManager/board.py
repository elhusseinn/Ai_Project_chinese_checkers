'''
1.represent board using 2D array coordinate system (with some of tree representation)
2.initialize the board with the appropriate position (1,2,3: for Player, 4,5,6: for PC, 0: for empty place to be played on, -1: for inaccessable index)
'''
from unittest import skip
import numpy

difficulty = 'easy'

def printBoard(board):
     for i in range(len(board)):
         print("\n")
         for j in range(len(board[i])):
            if(bool(board[i][j]==-1)):
                print(" ", end = ' ')
            elif(board[i][j]==0):
                print ("0", end = ' ')
            elif(board[i][j]==1):
                print("1", end = ' ') 
            elif(board[i][j]==2):
                print("2", end = ' ')

def init_board():
    board = numpy.full((17, 25), -1)

# Green is 1   To Human
    board[0][12] = 1
    board[1][11] = 1
    board[1][13] = 1
    board[2][10] = 1
    board[2][12] = 1
    board[2][14] = 1
    board[3][9]  = 1
    board[3][11] = 1
    board[3][13] = 1
    board[3][15] = 1

# playground2

    board[4][18] = 0
    board[4][20] = 0
    board[4][22] = 0
    board[4][24] = 0
    board[5][19] = 0
    board[5][21] = 0
    board[5][23] = 0
    board[6][20] = 0
    board[6][22] = 0
    board[7][21] = 0


# playground3

    board[9][21]  = 0
    board[10][20] = 0
    board[10][22] = 0
    board[11][19] = 0
    board[11][21] = 0
    board[11][23] = 0
    board[12][18] = 0
    board[12][20] = 0
    board[12][22] = 0
    board[12][24] = 0


# Red is 2 To PC

    board[13][9]  = 2
    board[13][11] = 2
    board[13][13] = 2
    board[13][15] = 2
    board[14][10] = 2
    board[14][12] = 2
    board[14][14] = 2
    board[15][11] = 2
    board[15][13] = 2
    board[16][12] = 2

# playground5
    board[9][3]  = 0
    board[10][2] = 0
    board[10][4] = 0
    board[11][1] = 0
    board[11][3] = 0
    board[11][5] = 0
    board[12][0] = 0
    board[12][2] = 0
    board[12][4] = 0
    board[12][6] = 0


# playground6

    board[4][0] = 0
    board[4][2] = 0
    board[4][4] = 0
    board[4][6] = 0
    board[5][1] = 0
    board[5][3] = 0
    board[5][5] = 0
    board[6][2] = 0
    board[6][4] = 0
    board[7][3] = 0


# play ground space initial is 0


# level 4
    board[4][8]  = 0
    board[4][10] = 0
    board[4][12] = 0
    board[4][14] = 0
    board[4][16] = 0
# level 5
    board[5][7]  = 0
    board[5][9]  = 0
    board[5][11] = 0
    board[5][13] = 0
    board[5][15] = 0
    board[5][17] = 0
# level 6
    board[6][6]  = 0
    board[6][8]  = 0
    board[6][10] = 0
    board[6][12] = 0
    board[6][14] = 0
    board[6][16] = 0
    board[6][18] = 0
# level 7
    board[7][5]  = 0
    board[7][7]  = 0
    board[7][9]  = 0
    board[7][11] = 0
    board[7][13] = 0
    board[7][15] = 0
    board[7][17] = 0
    board[7][19] = 0
# level 8
    board[8][4]  = 0
    board[8][6]  = 0
    board[8][8]  = 0
    board[8][10] = 0
    board[8][12] = 0
    board[8][14] = 0
    board[8][16] = 0
    board[8][18] = 0
    board[8][20] = 0
# level 9
    board[9][5]  = 0
    board[9][7]  = 0
    board[9][9]  = 0
    board[9][11] = 0
    board[9][13] = 0
    board[9][15] = 0
    board[9][17] = 0
    board[9][19] = 0
# level 10
    board[10][6]  = 0
    board[10][8]  = 0
    board[10][10] = 0
    board[10][12] = 0
    board[10][14] = 0
    board[10][16] = 0
    board[10][18] = 0
# level 11

    board[11][7]  = 0
    board[11][9]  = 0
    board[11][11] = 0
    board[11][13] = 0
    board[11][15] = 0
    board[11][17] = 0

# level 12
    board[12][8]  = 0
    board[12][10] = 0
    board[12][12] = 0
    board[12][14] = 0
    board[12][16] = 0

    return board


# if human wins retrun 1 >>>>> if pc wins return 0 <<<<< if none win return -1
def checkWin(board):
    # if all (1)green colors is on the other side then Human win
    if board[13][9] == 1 and board[13][11] == 1 and board[13][13] == 1 and board[13][15] == 1 and board[14][10] == 1 and board[14][12] == 1 and board[14][14] == 1 and board[15][11] == 1 and board[15][13] == 1 and board[16][12] == 1:

      return 1
    # if all (4)Red colors is on the other side then Pc win
    elif board[0][12] == 2 and board[1][11] == 2 and board[1][13] == 2 and board[2][10] == 2 and board[2][12] == 2 and board[2][14] == 2 and board[3][9] == 2 and board[3][11] == 2 and board[3][13] == 2 and board[3][15] == 2:

        return 0

    else:
        return -1


# Jump Moves Directions

def getJumpTopRight(board, backlevel, backindex, level, index):
    arrOfMoves = []
    newLevel = level-1
    newIndex = index+1
    if newLevel == backlevel and newIndex == backindex:
        skip
    elif board[newLevel][newIndex] == 1 or board[newLevel][newIndex] == 2:
        newLevel = newLevel-1
        newIndex = newIndex+1  # get the topRight of TopRight
        if board[newLevel][newIndex] == 0:
           arrOfMoves.append([newLevel, newIndex])
           newArrOfMoves = getJumpMoves(
               board, newLevel+1, newIndex-1, newLevel, newIndex)
           arrOfMoves.extend(newArrOfMoves)
    return arrOfMoves


def getJumpRight(board, backlevel, backindex, level, index):
    arrOfMoves = []
    newLevel = level
    newIndex = index+2
    if newLevel == backlevel and newIndex == backindex:
            skip
    elif board[newLevel][newIndex] == 1 or board[newLevel][newIndex] == 2:
         newLevel = newLevel
         newIndex = newIndex+2  # get the Right of Right
         if board[newLevel][newIndex] == 0:
              arrOfMoves.append([newLevel, newIndex])
              newArrOfMoves = getJumpMoves(
                  board, newLevel, newIndex-2, newLevel, newIndex)
              arrOfMoves.extend(newArrOfMoves)
    return arrOfMoves


def getJumpDownRight(board, backlevel, backindex, level, index):
    arrOfMoves = []
    newLevel = level+1
    newIndex = index+1
    if newLevel == backlevel and newIndex == backindex:
            skip
    elif board[newLevel][newIndex] == 1 or board[newLevel][newIndex] == 2:
         newLevel = newLevel+1
         newIndex = newIndex+1  # get the DownRight of DownRight
         if board[newLevel][newIndex] == 0:
              arrOfMoves.append([newLevel, newIndex])
              newArrOfMoves = getJumpMoves(
                  board, newLevel-1, newIndex-1, newLevel, newIndex)
              arrOfMoves.extend(newArrOfMoves)

    return arrOfMoves


def getJumpTopLeft(board, backlevel, backindex, level, index):
    arrOfMoves = []
    newLevel = level-1
    newIndex = index-1
    if newLevel == backlevel and newIndex == backindex:
            skip
    elif board[newLevel][newIndex] == 1 or board[newLevel][newIndex] == 2:
         # get the TopLeft of TopLeftewLevel=newLevel-1
         newIndex = newIndex-1
         if board[newLevel][newIndex] == 0:
              arrOfMoves.append([newLevel, newIndex])
              newArrOfMoves = getJumpMoves(
                  board, newLevel+1, newIndex+1, newLevel, newIndex)
              arrOfMoves.extend(newArrOfMoves)
    return arrOfMoves


def getJumpLeft(board, backlevel, backindex, level, index):
    arrOfMoves = []
    newLevel = level
    newIndex = index-2
    if newLevel == backlevel and newIndex == backindex:
            skip
    elif board[newLevel][newIndex] == 1 or board[newLevel][newIndex] == 2:
         newLevel = newLevel
         newIndex = newIndex-2  # get the Left of Left
         if board[newLevel][newIndex] == 0:
              arrOfMoves.append([newLevel, newIndex])
              newArrOfMoves = getJumpMoves(
                  board, newLevel, newIndex+2, newLevel, newIndex)
              arrOfMoves.extend(newArrOfMoves)
    return arrOfMoves


def getJumpDownLeft(board, backlevel, backindex, level, index):
    arrOfMoves = []
    newLevel = level+1
    newIndex = index-1
    if newLevel == backlevel and newIndex == backindex:
        skip
    elif board[newLevel][newIndex] == 1 or board[newLevel][newIndex] == 2:
           newLevel = newLevel+1
           newIndex = newIndex-1  # get the DownLeft of DownLeft
           if board[newLevel][newIndex] == 0:
              arrOfMoves.append([newLevel, newIndex])
              newArrOfMoves = getJumpMoves(
                  board, newLevel-1, newIndex+1, newLevel, newIndex)
              arrOfMoves.extend(newArrOfMoves)
    return arrOfMoves


def getJumpMoves(board, backlevel, backindex, level, index):
    arrOfMoves = []

    # TopRight
    newArrOfMoves = getJumpTopRight(board, backlevel, backindex, level, index)
    arrOfMoves.extend(newArrOfMoves)

    # Right
    newArrOfMoves = getJumpRight(board, backlevel, backindex, level, index)
    arrOfMoves.extend(newArrOfMoves)

    # DownRight

    newArrOfMoves = getJumpDownRight(board, backlevel, backindex, level, index)
    arrOfMoves.extend(newArrOfMoves)

    # TopLeft
    newArrOfMoves = getJumpTopLeft(board, backlevel, backindex, level, index)
    arrOfMoves.extend(newArrOfMoves)

    # Left
    newArrOfMoves = getJumpLeft(board, backlevel, backindex, level, index)
    arrOfMoves.extend(newArrOfMoves)

    # DownLeft
    newArrOfMoves = getJumpDownLeft(board, backlevel, backindex, level, index)
    arrOfMoves.extend(newArrOfMoves)

    return arrOfMoves


# Moves Directions
def getTopRight(board, level, index):
    # TopRight
    arrOfMoves = []
    newLevel = level-1
    newIndex = index+1
    if newLevel > 16 or newIndex > 24:
        skip
    elif board[newLevel][newIndex] == 0:
        arrOfMoves.append([newLevel, newIndex])
    # check top right if have value
    elif board[newLevel][newIndex] == 1 or board[newLevel][newIndex] == 2:
        newLevel = newLevel-1
        newIndex = newIndex+1  # get the topRight of TopRight
        if newLevel > 16 or newIndex > 24:
            skip
        elif board[newLevel][newIndex] == 0:
           arrOfMoves.append([newLevel, newIndex])
           newArrOfMoves = getJumpMoves(
               board, newLevel+1, newIndex-1, newLevel, newIndex)
           arrOfMoves.extend(newArrOfMoves)

    return arrOfMoves


def getRight(board, level, index):
    arrOfMoves = []
    newLevel = level
    newIndex = index+2
    if newLevel > 16 or newIndex > 24:
        skip
    elif board[newLevel][newIndex] == 0:
        arrOfMoves.append([newLevel, newIndex])
    elif board[newLevel][newIndex] == 1 or board[newLevel][newIndex] == 2:
         newLevel = newLevel
         newIndex = newIndex+2  # get the Right of Right
         if newLevel > 16 or newIndex > 24:
            skip
         elif board[newLevel][newIndex] == 0:
              arrOfMoves.append([newLevel, newIndex])
              newArrOfMoves = getJumpMoves(
                  board, newLevel, newIndex-2, newLevel, newIndex)
              arrOfMoves.extend(newArrOfMoves)
    return arrOfMoves


def getDownRight(board, level, index):
    arrOfMoves = []
    newLevel = level+1
    newIndex = index+1
    if newLevel > 16 or newIndex > 24:
        skip
    elif board[newLevel][newIndex] == 0:
        arrOfMoves.append([newLevel, newIndex])
    elif board[newLevel][newIndex] == 1 or board[newLevel][newIndex] == 2:
         newLevel = newLevel+1
         newIndex = newIndex+1  # get the DownRight of DownRight
         if newLevel > 16 or newIndex > 24:
            skip
         elif board[newLevel][newIndex] == 0:
              arrOfMoves.append([newLevel, newIndex])
              newArrOfMoves = getJumpMoves(
                  board, newLevel-1, newIndex-1, newLevel, newIndex)
              arrOfMoves.extend(newArrOfMoves)

    return arrOfMoves


def getTopLeft(board, level, index):
    arrOfMoves = []
    newLevel = level-1
    newIndex = index-1
    if newLevel > 16 or newIndex > 24:
        skip
    elif board[newLevel][newIndex] == 0:
        arrOfMoves.append([newLevel, newIndex])
    elif board[newLevel][newIndex] == 1 or board[newLevel][newIndex] == 2:
         newLevel = newLevel-1
         newIndex = newIndex-1  # get the TopLeft of TopLeft
         if newLevel > 16 or newIndex > 24:
            skip
         elif board[newLevel][newIndex] == 0:
              arrOfMoves.append([newLevel, newIndex])
              newArrOfMoves = getJumpMoves(
                  board, newLevel+1, newIndex+1, newLevel, newIndex)
              arrOfMoves.extend(newArrOfMoves)

    return arrOfMoves


def getLeft(board, level, index):
    arrOfMoves = []
    newLevel = level
    newIndex = index-2
    if newLevel > 16 or newIndex > 24:
        skip
    elif board[newLevel][newIndex] == 0:
        arrOfMoves.append([newLevel, newIndex])
    elif board[newLevel][newIndex] == 1 or board[newLevel][newIndex] == 2:
         newLevel = newLevel
         newIndex = newIndex-2  # get the Left of Left
         if newLevel > 16 or newIndex > 24:
            skip
         elif board[newLevel][newIndex] == 0:
              arrOfMoves.append([newLevel, newIndex])
              newArrOfMoves = getJumpMoves(
                  board, newLevel, newIndex+2, newLevel, newIndex)
              arrOfMoves.extend(newArrOfMoves)
    return arrOfMoves


def getDownLeft(board, level, index):
    arrOfMoves = []
    newLevel = level+1
    newIndex = index-1
    if newLevel > 16 or newIndex > 24:
        skip
    elif board[newLevel][newIndex] == 0:
        arrOfMoves.append([newLevel, newIndex])
    elif board[newLevel][newIndex] == 1 or board[newLevel][newIndex] == 2:
           newLevel = newLevel+1
           newIndex = newIndex-1  # get the DownLeft of DownLeft
           if newLevel > 16 or newIndex > 24:
             skip
           elif board[newLevel][newIndex] == 0:
              arrOfMoves.append([newLevel, newIndex])
              newArrOfMoves = getJumpMoves(
                  board, newLevel-1, newIndex+1, newLevel, newIndex)
              arrOfMoves.extend(newArrOfMoves)
    return arrOfMoves


def getHumanMovesInsideGoal(arrOfMoves):    
    newArrOfMoves=[]
    for i in range(len(arrOfMoves)):
          if not (arrOfMoves[i][0]<13):
                 newArrOfMoves.append(arrOfMoves[i])
  
    return newArrOfMoves 

def getComputerMovesInsideGoal(arrOfMoves):    
    newArrOfMoves=[]
    for i in range(len(arrOfMoves)):
          if not (arrOfMoves[i][0]>3):
                 newArrOfMoves.append(arrOfMoves[i])
  
    return newArrOfMoves 

def getAvailableMoves(board,level,index):
    arrOfMoves=[]

    # TopRight
    newArrOfMoves=getTopRight(board,level,index)
    arrOfMoves.extend(newArrOfMoves)
    
    # Right
    
    newArrOfMoves=getRight(board,level,index)
    arrOfMoves.extend(newArrOfMoves)
    


    # DownRight
    
    newArrOfMoves=getDownRight(board,level,index)
    arrOfMoves.extend(newArrOfMoves)

    # TopLeft
    
    newArrOfMoves=getTopLeft(board,level,index)
    arrOfMoves.extend(newArrOfMoves)


    # Left
   
    newArrOfMoves=getLeft(board,level,index)
    arrOfMoves.extend(newArrOfMoves)




    # DownLeft
    newArrOfMoves=getDownLeft(board,level,index)
    arrOfMoves.extend(newArrOfMoves)
    
    if board[level][index]==1 and level>=13 :
        arrOfMoves=getHumanMovesInsideGoal(arrOfMoves)
    elif board[level][index]==2  and level<=3 :
         arrOfMoves=getComputerMovesInsideGoal(arrOfMoves)  


    return arrOfMoves
