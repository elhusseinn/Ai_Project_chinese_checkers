from PC_Move_Controller import controller as controller
from asyncio import sleep
from GameManager import board as BD
import sys

sys.setrecursionlimit(8000)

# for i in range(15):
#   BD.printBoard(controller.PC_Move(board, 2))
#  print(controller.calculate_heuristic(board))


board = BD.init_board()


def Gameplaying(board, stateDiffc):
    print("ChienesCheckerGame :Pc will play with red and you with Green ")
    print("You will play First and have board u will choose the level and index that u want to move")
    print("Then enter where do you want to move it to with level and index of it ")

    while (True):
        print('\n')
        BD.printBoard(board)
        while (True):

            # >>>>>>>>>>>>>>>HumanPlay<<<<<<<<<<<

            print('\n')
            print("Choose The element you want to Move:")
            print('\n')
            level = int(input("Enter the Level: "))
            print('\n')
            index = int(input("Enter the Index: "))
            print('\n')
            if (board[level][index] == 1):
                arrOfMoves = BD.getAvailableMoves(board, level, index)
                print("Choose The place you want to put it in:")
                print('\n')
                levelMove = int(input("Enter the Level: "))
                print('\n')
                indexMove = int(input("Enter the Index: "))
                print('\n')
                if ([levelMove, indexMove] in arrOfMoves):
                    board[level][index] = 0
                    board[levelMove][indexMove] = 1
                    BD.printBoard(board)

                    print('\n')
                    break
                else:
                    BD.printBoard(board)
                    print(
                        "\nCant Move To This One ! Pick your Marble color  and your Destination again please ")
                    3

            else:
                BD.printBoard(board)
                print("\nCant Move This One ! Pick your Marble color please! ")

        # >>>>>>>>>>>>>>Check win<<<<<<<<<<<<<<<
        stateWinNum = BD.checkWin(board)
        if (stateWinNum == 1):
            print("Congratulation You Win !")
            print("Game Over ")
            break
        elif (stateWinNum == 2):
            print("You lost ,Good Luck Next Time !")
            break

        # >>>>>>>>>>>>>PC Play<<<<<<<<<<
        if (stateDiffc == 1):
            board = controller.PC_Move(board, 1)
        elif (stateDiffc == 2):
            board = controller.PC_Move(board, 3)
        elif (stateDiffc == 3):
            board = controller.PC_Move(board, 5)

        # >>>>>>>>>>>>>>>Check win<<<<<<<<<<<<<<
        stateWinNum = BD.checkWin(board)
        if (stateWinNum == 1):
            print("Congratulation You Win !")
            print("Game Over ")
            break
        elif (stateWinNum == 2):
            print("You lost ,Good Luck Next Time !")


print("Welcome to our game , you can choose the Difficulty of the game by pick number: ")
print("1-Easy")
print("2-Meduim")
print("3-Hard")
stateDiffc = int(input("Enter your number : "))
Gameplaying(board, stateDiffc)