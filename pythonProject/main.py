import pygame

# Initialize the pygame
pygame.init()

# Create the screen
screen = pygame.display.set_mode((800, 600))

# Title and Icon(32px)
pygame.display.set_caption('Space Invaders')
icon = pygame.image.load('ufo.png')
pygame.display.set_icon(icon)

# Player(64px)
playerImg = pygame.image.load('player.png')
playerX = 370
playerY = 480
playerX_change = 0


def player(x, y):
    screen.blit(playerImg, (x, y))


# Game loop
running = True
while running:
    # RGB (0-255) - Red, Green, Blue
    screen.fill((0, 0, 0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # if keystroke is pressed check whether is left or right
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                playerX_change = -0.3
            if event.key == pygame.K_RIGHT:
                playerX_change = 0.3
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                playerX_change = 0

    playerX += playerX_change

    # Border left/right
    if playerX <= 0:
        playerX = 0
    # 800px-64px=736
    elif playerX >= 736:
        playerX = 736

    player(playerX, playerY)
    pygame.display.update()
