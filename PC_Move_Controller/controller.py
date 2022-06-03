from GameManager import board as BD
from numpy import *

# function that take the board and returns all the indexes taken by PC
def get_board_positions(board, x):
    currentPosition = []
    for i in range (17):
        for j in range (25):
            if board[i][j] == x:
                currentPosition.append([i,j])
    return currentPosition





# function that loops through every position (the PC holds on the board) and generate every state to each (GENERATE SEARCH SPACE)
    # according to the difficulty generate another levels or not

#draft function:
#goal : generate all possible states from a given state 
def generateStates(board): # make another function that takes all those possible moves and generate states from it
    tempBoard = board.copy()
    states = [] 
    positions = get_board_positions(board,2) # gets all the positions of all my marbles in the board
    for position in positions:
        level = position[0]
        index = position[1]
        availableMoves = BD.getAvailableMoves(board,level,index)
        for move in availableMoves:
            tempBoard[level][index]  = 0          # removes the marble from the current position
            tempBoard[move[0]][move[1]] = 2
            states.append(tempBoard)
            tempBoard = board.copy()

    return states




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


# function that applies minimax , uses heuristic and generateSearchSpace functions
