import pygame

# Intialize the pygame
pygame.init()

# window screen
window_screen = pygame.display.set_mode((800,600))

# Title / Icon
pygame.display.set_caption('JA\'s Firewall Invader')
icon = pygame.image.load('image/computer.png')
pygame.display.set_icon(icon)

# Player
player_Image = pygame.image.load('image/firewall_logo.png')
playerX = 370
playerY = 500

def player():
    # draw the player onto the screen
    window_screen.blit(player_Image,(playerX,playerY))


#Game Loop
running = True
while running:
    # Has red,green, blue
    window_screen.fill((0, 0, 0))
    # Background Image


    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    player()
    pygame.display.update()


