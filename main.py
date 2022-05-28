import pygame

pygame.init()

screen = pygame.display.set_mode((600, 690))

pygame.display.set_caption("Chinese checkers")
icon = pygame.image.load("chinese-checkers(2).png")
pygame.display.set_icon(icon)

# Player
playerimg = pygame.image.load("spaceship.png")
playerX = 370
playerY = 480
playerX_change = 0


# Enemy
# enemyimg = pygame.image.load("ghost(1).png")
# enemyX = random.randint(0, 800)
# enemyY = random.randint(50, 150)
# enemyX_change = 0.3
# enemyY_change = 0


def player(x, y):
    screen.blit(playerimg, (x, y))


# def enemy(x, y):
#     screen.blit(enemyimg, (x, y))

class marble:
    def __init__(self, x, y, color):
        self.x = x
        self.y = y
        self.color = color

m1 = marble(500,400,"blue")
m1.x=500
m1.y = 400
m1.color = "red"
print(m1.color)


def move(x, y, color):
    if color == "red":
        screen.blit(pygame.image.load("circle.png"), (x, y))
    elif color == "blue":
        screen.blit(pygame.image.load("Blue.png"), (x, y))
    elif color == "yellow":
        screen.blit(pygame.image.load('yellow.png'), (x, y))
    elif color == "black":
        screen.blit(pygame.image.load('black.png'), (x, y))
    elif color == "green":
        screen.blit(pygame.image.load('green.png'), (x, y))
    elif color == "white":
        screen.blit(pygame.image.load('white.png'), (x, y))
    else:
        print("invalid color")


background = pygame.image.load('FP9BSHTG6MPPU78.png')
running = True
while running:
    screen.fill((0, 0, 150))
    # background image
    screen.blit(background, (0, 0))
    # playerX+=0.2
    # print(playerX)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                playerX_change = -0.3
            if event.key == pygame.K_RIGHT:
                playerX_change = 0.3
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_RIGHT or event.key == pygame.K_LEFT:
                playerX_change = 0
    # RGB = Red , Green , Blue
    playerX += playerX_change

    if playerX <= 0:
        playerX = 0
    elif playerX > 736:
        playerX = 736

    # enemyX += enemyX_change
    #
    # if enemyX <= 0:
    #     enemyXchange = 0.3
    # elif enemyX >= 736:
    #     enemyXchange = -0.3
    #

    # player(playerX, playerY)
    # enemy(enemyX, enemyY)
    move(285, 655, "blue")
    move(285, 655, "blue")
    # move(309, 615, "blue")
    move(260, 614, "blue")
    move(309, 615, "red")
    move(237, 573, "red")
    move(285, 573, "blue")
    move(332, 573, "red")
    move(356, 533, "red")
    move(262, 533, "red")

    move(309, 533, "blue")

    move(262 - 48, 533, "red")
    # move(443 - 17, 509 - 17, "red")
    move(490 - 17, 509 - 17, "red")
    move(443 - 17, 509 - 17, "yellow")
    move(585 - 18, 509 - 17, "black")
    move(560 - 16, 468 - 17, "red")

    pygame.display.update()
