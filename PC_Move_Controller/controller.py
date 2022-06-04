from turtle import position
from GameManager import board as BD
from numpy import *
import math

# function that take the board and returns all the indexes taken by PC
def get_board_positions(board, x):
    currentPosition = []
    for i in range (17):
        for j in range (25):
            if board[i][j] == x:
                currentPosition.append([i,j])
    return currentPosition

# function for hueristic calculation (takes a state and return a value)
def get_deepest_empty_goal(board, player):
    # deepestLevel = None
    # deepestIndex = None
    # if player == 1: # goal starts at [16][12]
    #     for level in range(0, 4):
    #         for index in range(9, 16):
    #             # if board[level][index] = 0 :
                    
                
    # elif player == 2: # goal starts at [0][12]
    #     return 0
    return 1

def eclidiean_distance(start, end):
        num1 = pow(end[0] - start[0], 2)
        num2 = pow(end[1] - start[1], 2)
        return sqrt(num1 + num2)

def calculate_heuristic(board):
    Ai_positions = get_board_positions(board, 2)
    player_positions = get_board_positions(board, 1)
    heurestic_Player = 0
    heurestic_AI = 0
    for position in Ai_positions:
        heurestic_AI += eclidiean_distance(position, [0,12])
    for position in player_positions:
        heurestic_Player += eclidiean_distance(position, [16,12])
    return heurestic_AI - heurestic_Player


def generateStates(board,x): # takes a state and a player type(1 for player, 2 for Ai) and return all the possible states
    tempBoard = board.copy()
    states = [] 
    positions = get_board_positions(board,x) # gets all the positions of all my marbles in the board
    for position in positions:
        level = position[0]
        index = position[1]
        availableMoves = BD.getAvailableMoves(board,level,index)
        for move in availableMoves:
            tempBoard[level][index]  = 0          # removes the marble from the current position
            tempBoard[move[0]][move[1]] = x       # put the marble in the next position which generates the state
            states.append(tempBoard)
            tempBoard = board.copy()

    return states

'''def getBestState(states):

    bestMove=[]
    for state in states:
            heuristic = calculate_heuristic(state)
            if (heuristic > bestheuristic):
                    bestheuristic = heuristic
                    bestMove = state
                   
    return bestMove
# function that applies minimax , uses heuristic and generateStates functions

def miniMax (board, depth, maximizingAgent): # takes board(cuurent state) , return the best move i can make in terms of [marble-> to position]
    result = BD.checkWin(board)
    bestMove = []
    bestheuristic= -math.inf
    # if(depth == 1 or result != -1):
    #      states = generateStates(board,maximizingAgent)
    #      return getBestState(states)
    
    

    if(maximizingAgent == 2):
        bestheuristic ,bestMove = maxValue(board,depth)
        
    else:
       bestheuristic ,bestMove = minValue(board,depth)
       
    return bestMove


def maxValue(state,depth):
    result = BD.checkWin(state)
    if(result!=-1):
        if(result ==1):
              return float('-inf'), None
        else:
            return float('inf'), None
    elif(depth==0):
        return calculate_heuristic(state) ,state
    
    heur=-math.inf
    maxState= None
    for state1 in generateStates(state,2):
        temp, _ = minValue(state,depth-1)
        if(heur<temp):
            heur=temp
            maxState=state1
    return heur,maxState

def minValue(state,depth):
    result = BD.checkWin(state)
    if(result!=-1):
        if(result ==1):
              return float('-inf'), None
        else:
            return float('inf'), None
    elif(depth==0):
        return calculate_heuristic(state) ,state

    heur = math.inf
    minState=None
    for state1 in generateStates(state,1):
        h1, _ = maxValue(state1,depth-1)
        if(heur>h1):
            heur=h1
            minState = state1
    return heur,minState'''

def miniMax(board, depth, maximizingAgent): # takes board(cuurent state) , return the best move i can make in terms of [marble-> to position]
    result = BD.checkWin(board)
    if(depth == 0 or result != -1):
        return calculate_heuristic(board)
    if(maximizingAgent == 2):
        finalScore = -math.inf
        # recursively get the states
        tempBoard = board.copy()
        positions = get_board_positions(board,maximizingAgent)
        for position in positions:
            level = position[0]
            index = position[1]
            availableMoves = BD.getAvailableMoves(board,level,index)
            for move in availableMoves:
                tempBoard[level][index]  = 0  # removes the marble from the current position
                tempBoard[move[0]][move[1]] = maximizingAgent   # put the marble in the next position which generates the state
                score = miniMax(tempBoard, depth-1, 1)
                tempBoard = board.copy()
                finalScore = max(finalScore, score)
        return finalScore
    else:
        finalScore = math.inf
        # here we recursively get the states
        tempBoard = board.copy()
        positions = get_board_positions(board,maximizingAgent)
        for position in positions:
            level = position[0]
            index = position[1]
            availableMoves = BD.getAvailableMoves(board,level,index)
            for move in availableMoves:
                tempBoard[level][index]  = 0          # removes the marble from the current position
                tempBoard[move[0]][move[1]] = maximizingAgent       # put the marble in the next position which generates the state
                score = miniMax(tempBoard, depth-1, 2)
                tempBoard = board.copy()
                finalScore = min(finalScore, score)
        return finalScore

def getBestMove(board, depth):
    bestPosition = None
    bestMove = None
    bestScore = -math.inf
    tempBoard = board.copy()
    positions = get_board_positions(board,2)
    for position in positions:
            level = position[0]
            index = position[1]
            availableMoves = BD.getAvailableMoves(board,level,index)
            for move in availableMoves:
                tempBoard[level][index]  = 0          # removes the marble from the current position
                tempBoard[move[0]][move[1]] = 2       # put the marble in the next position which generates the state
                score = miniMax(tempBoard,depth-1, 1)
                if(score > bestScore):
                    bestScore = score
                    bestPosition = position
                    bestMove = move
                tempBoard = board.copy()
    return bestPosition,bestMove


def PC_Move(board, depth):
    move = getBestMove(board, depth)
    source = move[0]
    destination = move[1]

    board[source[0]][source[1]] = 0
    board[destination[0]][destination[1]] = 2

    return board


