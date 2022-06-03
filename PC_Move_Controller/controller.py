from GameManager import board as BD

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

def generateSearchSpace(board): # make another function that takes all those possible moves and generate states from it 
    moves = [] #
    positions = get_PC_board_positions(board) # gets all the positions of all my marbles in the board
    for position in positions:
        level = position[0]
        index = position[1]
        moves.append([position,BD.getAvailableMoves(board,level,index)]) # append to the list all the moves i can play 
    return moves




# function for hueristic calculation (takes a state and return a value)





# function that applies minimax , uses heuristic and generateSearchSpace functions
