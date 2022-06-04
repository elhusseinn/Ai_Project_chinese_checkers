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

    board[9][21] = 0
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

    board[13][9] = 2
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
    board[9][3] = 0
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
    board[4][8] = 0
    board[4][10] = 0
    board[4][12] = 0
    board[4][14] = 0
    board[4][16] = 0
# level 5
    board[5][7] = 0
    board[5][9] = 0
    board[5][11] = 0
    board[5][13] = 0
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
    board[7][13] = 0
    board[7][15] = 0
    board[7][17] = 0
    board[7][19] = 0
# level 8
    board[8][4] = 0
    board[8][6] = 0
    board[8][8] = 0
    board[8][10] = 0
    board[8][12] = 0
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



       
#topright=1
#right=2
#downright=3
#topleft=4 
#left=5
#downleft=6



def getJumpMoves(board, murblesIndexs,level, index):
  usedMurbles=[[level,index]]
  arrOfMoves=[]
  i=0
  while(i==0 and len(murblesIndexs)!=0):  
   level=murblesIndexs[0][0]
   index=murblesIndexs[0][1]
   direct=murblesIndexs[0][2]
   if not ( [level,index] in usedMurbles): 
    usedMurbles.append([level,index])  
    # TopRight
    if  index < 24 and direct==1:
     if(board[level-1][index+1]==0): 
         arrOfMoves.append([level-1,index+1])
         murblesIndexs.extend(getMurblesAround(board,level-1,index+1))
    # Right
    if  index < 23 and direct==2:
     if(board[level][index+2]==0):    
        arrOfMoves.append([level,index+2])
        murblesIndexs.extend(getMurblesAround(board,level,index+2))
    # DownRight
    if  level < 16 and index<24 and  direct==3: 
     if(board[level+1][index+1]==0):        
       arrOfMoves.append([level+1,index+1])
       murblesIndexs.extend(getMurblesAround(board,level+1,index+1))
      
    # TopLeft
    if( direct==4):
     if(board[level-1][index-1]==0):    
      arrOfMoves.append([level-1,index-1])
      murblesIndexs.extend(getMurblesAround(board,level-1,index-1))
    # Left
    if( direct==5):
     if(board[level][index-2]==0):    
      arrOfMoves.append([level,index-2])
      murblesIndexs.extend(getMurblesAround(board,level,index-2))
    # DownLeft
    if(level<16 and direct==6):
     if(board[level+1][index-1]==0):    
        arrOfMoves.append([level+1,index-1])
        murblesIndexs.extend(getMurblesAround(board,level+1,index-1))
    
    
    
    if len(murblesIndexs)==1:
        i=-1
    murblesIndexs.remove(murblesIndexs[0])
   else:
        if len(murblesIndexs)==1:
            i=-1
        murblesIndexs.remove(murblesIndexs[0]) 
  return arrOfMoves
 
  
def getMurblesAround(board,level,index):
#topright=1
#right=2
#downright=3
#topleft=4 
#left=5
#downleft=6
    murblesIndexs=[]
     # TopRight
    if  index < 24:
         if(board[level-1][index+1]>0):
           murblesIndexs.append([level-1,index+1,1])
    # Right
    if  index < 23:
     if(board[level][index+2]>0):
        murblesIndexs.append([level,index+2,2])
    # DownRight
    if  level < 16 and index<24: 
     if(board[level+1][index+1]>0):
       murblesIndexs.append([level+1,index+1,3])   
    # TopLeft
    if(board[level-1][index-1]>0):
      murblesIndexs.append([level-1,index-1,4])
    # Left
    if(board[level][index-2]>0):
      murblesIndexs.append([level,index-2,5])
    # DownLeft
    if(level<16):
     if(board[level+1][index-1]>0):
        murblesIndexs.append([level+1,index-1,6])
   
    return murblesIndexs      

# Moves Directions
def getTopRight(board, level, index):
    # TopRight
    arrOfMoves = []
    newLevel = level-1
    newIndex = index+1
    if newLevel > 16 or newIndex > 24:
        return arrOfMoves
    elif board[newLevel][newIndex] == 0 :
        arrOfMoves.append([newLevel, newIndex])

    return arrOfMoves


def getRight(board,level, index):
    arrOfMoves = []
    newLevel = level
    newIndex = index+2
    if newLevel > 16 or newIndex > 24:
        return arrOfMoves
    elif board[newLevel][newIndex] == 0 :
        arrOfMoves.append([newLevel, newIndex])
    return arrOfMoves
def getDownRight(board, level, index):
    arrOfMoves = []
    newLevel = level+1
    newIndex = index+1
    if newLevel > 16 or newIndex > 24:
        return arrOfMoves
    elif board[newLevel][newIndex] == 0 :
        arrOfMoves.append([newLevel, newIndex])

    return arrOfMoves


def getTopLeft(board ,level, index):
    arrOfMoves = []
    newLevel = level-1
    newIndex = index-1
    if newLevel > 16 or newIndex > 24:
        return arrOfMoves
    elif board[newLevel][newIndex] == 0 :
        arrOfMoves.append([newLevel, newIndex])
    

    return arrOfMoves


def getLeft(board, level, index):
    arrOfMoves = []
    newLevel = level
    newIndex = index-2
    if newLevel > 16 or newIndex > 24:
        return arrOfMoves
    elif board[newLevel][newIndex] == 0 :
        arrOfMoves.append([newLevel, newIndex])
   
    return arrOfMoves


def getDownLeft(board, level, index):
    arrOfMoves = []
    newLevel = level+1
    newIndex = index-1
    if newLevel > 16 or newIndex > 24:
        return arrOfMoves
    elif board[newLevel][newIndex] == 0 :
        arrOfMoves.append([newLevel, newIndex])

    return arrOfMoves


def getHumanMovesInsideGoal(arrOfMoves):
    newArrOfMoves = []
    for i in range(len(arrOfMoves)):
        if not (arrOfMoves[i][0] < 13):
            newArrOfMoves.append(arrOfMoves[i])

    return newArrOfMoves


def getComputerMovesInsideGoal(arrOfMoves):
    newArrOfMoves = []
    for i in range(len(arrOfMoves)):
        if not (arrOfMoves[i][0] > 3):
            newArrOfMoves.append(arrOfMoves[i])

    return newArrOfMoves


def getAvailableMoves(board, level, index):
    arrOfMoves = []
    murblesIndexs=[]
    # TopRight
    newArrOfMoves = getTopRight(board,level, index)
    arrOfMoves.extend(newArrOfMoves)

    # Right

    newArrOfMoves = getRight(board,level, index)
    arrOfMoves.extend(newArrOfMoves)

    # DownRight

    newArrOfMoves = getDownRight(board,level, index)
    arrOfMoves.extend(newArrOfMoves)

    # TopLeft

    newArrOfMoves = getTopLeft(board,level, index)
    arrOfMoves.extend(newArrOfMoves)

    # Left

    newArrOfMoves = getLeft(board,level, index)
    arrOfMoves.extend(newArrOfMoves)

    # DownLeft
    newArrOfMoves = getDownLeft(board,level, index)
    arrOfMoves.extend(newArrOfMoves)
  
    murblesIndexs=getMurblesAround(board,level,index)


    arrOfMoves.extend(getJumpMoves(board,murblesIndexs,level,index))
    if board[level][index] == 1 and level >= 13:
        arrOfMoves = getHumanMovesInsideGoal(arrOfMoves)
    elif board[level][index] == 2 and level <= 3:
        arrOfMoves = getComputerMovesInsideGoal(arrOfMoves)

    return arrOfMoves


def printBoard(board):

    print("   ", end=' ')
    for i in range(0, 25, 1):
        if(i < 10):
            print(i, end='   ')
        else:
            print(i, end='  ')
    for i in range(len(board)):
        print("\n")
        print(i, end=' ')
        print(" ", end=' ')
        for j in range(len(board[i])):
            if(bool(board[i][j] == -1)):
                print(" ", end='   ')
            elif(board[i][j] == 0):
                print("*", end='   ')
            elif(board[i][j] == 1):
                print("G", end='   ')
            elif(board[i][j] == 2):
                print("R", end='   ')