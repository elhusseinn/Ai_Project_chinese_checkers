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

def calculate_heuristic(board):
    Ai_positions = get_board_positions(board, 2)
    player_positions = get_board_positions(board, 1)
    heurestic_Player = 0
    heurestic_AI = 0
    for position in Ai_positions:
        heurestic_AI+=(abs(position[0]-0)+abs(position[1]-12))
    for position in player_positions:
        heurestic_Player += (abs(position[0]-16)+abs(position[1]-12))
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

# function that applies minimax , uses heuristic and generateStates functions

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
