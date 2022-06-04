import numpy
import pygame
from GameManager import board as BD
from PC_Move_Controller import controller as controller

pygame.init()

screen = pygame.display.set_mode((700, 400))

pygame.display.set_caption("Chinese checkers")
icon = pygame.image.load("chinese-checkers(2).png")
pygame.display.set_icon(icon)

# board


board = numpy.ones((17, 25))
board *= -1

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
CELL_SIZE = 20

marble_rect = []

def animation(moves=[], clicked_token=None):
    colors = [(240, 230, 230), "red", "green"]
    moves.append(clicked_token)
    for i in range(0, 17):
        for j in range(0, 25):
            if board[i][j] >= 0:
                rect = pygame.Rect(j * CELL_SIZE, i *
                                   CELL_SIZE, CELL_SIZE, CELL_SIZE)
                marble_rect.append(pygame.draw.rect(
                    screen, colors[int(board[i][j])], rect, border_radius=20))
            if [i, j] in moves:
                test_circle = pygame.image.load('Pics/circle.png')
                test_circle = pygame.transform.scale(
                    test_circle, (CELL_SIZE + 2, CELL_SIZE + 2))
                screen.blit(
                    test_circle, (j * CELL_SIZE - 1, i * CELL_SIZE - 1))


def get_pos(x, y):
    coox = int(x / 20)
    cooy = int(y / 20)
    print(coox, cooy)
    return [coox, cooy]

class marble:
    # m1 = marble()
    # def move(x, y, color):
    #     if color == "red":
    #         screen.blit(pygame.image.load("Pics/red.png"), (x, y))
    #     elif color == "blue":
    #         screen.blit(pygame.image.load("Pics/Blue.png"), (x, y))
    #     elif color == "yellow":
    #         screen.blit(pygame.image.load('Pics/yellow.png'), (x, y))
    #     elif color == "black":
    #         screen.blit(pygame.image.load('Pics/black.png'), (x, y))
    #     elif color == "green":
    #         screen.blit(pygame.image.load('Pics/green.png'), (x, y))
    #     elif color == "white":
    #         screen.blit(pygame.image.load('Pics/white.png'), (x, y))
    #     else:
    #         print("invalid color")

    def move(self, lastP, newP):
        board[newP[0]][newP[1]] = board[lastP[0]][lastP[1]]
        board[lastP[0]][lastP[1]] = 0

    def marble(self):
        colors = [(240, 230, 230), "red", "green"]
        for i in range(0, 17):
            for j in range(0, 25):
                if board[i][j] >= 0:
                    rect = pygame.Rect(
                        j * CELL_SIZE, i * CELL_SIZE, CELL_SIZE, CELL_SIZE)
                    marble_rect.append(pygame.draw.rect(screen, colors[int(board[i][j])], rect, border_radius=20))

    lasted_selected_token = []
    player_valid_moves =[]
    playerwon = False
    AiWon = False
    running = True
    screen.fill((105, 105, 105))
    while running:
        # background image
        # screen.blit(background, (0, 0))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                cleared_places = [s for s in marble_rect if s.collidepoint(mouse_pos)]
                print(mouse_pos)
                if cleared_places:
                    clicked_token = get_pos(cleared_places[0].x, cleared_places[0].y)
                    if board[clicked_token[0]][clicked_token[1]] == 1:
                        if clicked_token == lasted_selected_token:
                            selected = False
                            last_selected_token = []
                            player_valid_moves = []
                        else:
                            player_valid_moves = BD.getAvailableMoves(board, clicked_token[1],clicked_token[0])
                            selected = True
                            # screen.fill((105, 105, 105))
                            animation(player_valid_moves, last_selected_token)
                    elif clicked_token in player_valid_moves:
                        move(last_selected_token, clicked_token)
                        # check for win function goes here
                        value = BD.checkWin(board)
                        if value == 1:
                            screen.blit("png-clipart-you-win-youtube-80-days-video-game-logo-win-game-text.png",700, 400)
                        elif value == 0:
                            screen.blit("png-clipart-you-win-youtube-80-days-video-game-logo-win-game-text.png", 700,
                                        400)
                        selected = False
                        last_selected_token = []
                        player_valid_moves = []
                        # screen.fill((105, 105, 105))
                        player_index = (player_index + 1) % 3
                        if player_index == 0:
                            player_index += 1
                        animation()

    

    clock = pygame.time.Clock()
    # move(pygame.mouse.get_pos()[0], pygame.mouse.get_pos()[1], "black")  # [11][3]

    # if pygame.mouse.get_pressed:
    #     print(pygame.mouse.get_pos())
    #     move(pygame.mouse.get_pos()[0], pygame.mouse.get_pos()[1], "black")

    pygame.display.update()



m1 = marble()
m1.x = 500
m1.y = 400
m1.color = "red"
print(m1.color)





def CoordinatConv(coordinate):
    y = 0
    if coordinate[1] == 0:
        y = 15
    elif coordinate[1] == 1:
        y = 39
    elif coordinate[1] == 2:
        y = 83
    elif coordinate[1] == 3:
        y = 122
    elif coordinate[1] == 4:
        y = 164
    elif coordinate[1] == 5:
        y = 204
    elif coordinate[1] == 6:
        y = 247
    elif coordinate[1] == 7:
        y = 289
    elif coordinate[1] == 8:
        y = 328
    elif coordinate[1] == 9:
        y = 370
    elif coordinate[1] == 10:
        y = 409
    elif coordinate[1] == 11:
        y = 452
    elif coordinate[1] == 12:
        y = 493
    elif coordinate[1] == 13:
        y = 535
    elif coordinate[1] == 14:
        y = 574
    elif coordinate[1] == 15:
        y = 614
    elif coordinate[1] == 16:
        y = 658

    x = (int)(((coordinate[1] / 2) * 48) + 13) - 16
    print(y)
    return (x, y)


marble_draging = False
# background = pygame.image.load('Pics/FP9BSHTG6MPPU78.png')
running = True

