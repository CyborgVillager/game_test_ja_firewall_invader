import pygame
from entites_movement import *

# Intialize the pygame
pygame.init()

# window screen
window_screen = pygame.display.set_mode((800, 600))

# Background
background = pygame.image.load('image/background.jpg')

# Title / Icon
pygame.display.set_caption('JA\'s Firewall Invader')
icon = pygame.image.load('image/computer.png')
pygame.display.set_icon(icon)



# Score
score_value = 0
font = pygame.font.Font('freesansbold.ttf', 32)

textX = 10
testY = 10

# Game Over
over_font = pygame.font.Font('freesansbold.ttf', 64)


def show_score(x, y):
    score = font.render("Score : " + str(score_value), True, (255, 255, 255))
    window_screen.blit(score, (x, y))


def game_over_text():
    over_text = over_font.render("GAME OVER", True, (255, 255, 255))
    window_screen.blit(over_text, (200, 250))


# Player
def player(x, y):  # new values for x & y are able to be drawn on the screen
    # draw the player onto the screen
    window_screen.blit(player_Image, (x, y))


def fire_bullet(x, y):
    global bullet_state
    bullet_state = "fire"
    window_screen.blit(bullet_Image, (x + 16, y + 10))



# Hostile Types
def hostile_spyware(x, y):  # new values for x & y are able to be drawn on the screen
    # draw the player onto the screen
    window_screen.blit(hostile_Spyware_Image, (x, y))


# Game Loop
running = True
while running:
    # Has red,green, blue
    window_screen.fill((0, 0, 0))
    # Background Image
    window_screen.blit(background,(0,0))
    # keystrokes
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        # sys will check if keystroke is pressed by user
        if event.type == pygame.KEYDOWN:
            print('A keystroke has been pressed')
            if event.key == pygame.K_LEFT:
                playerX_change = left_up_player_speed
            if event.key == pygame.K_RIGHT:
                playerX_change = right_down_player_speed
            if event.key == pygame.K_UP:
                playerY_change = left_up_player_speed
            if event.key == pygame.K_DOWN:
                playerY_change = right_down_player_speed
            if event.key == pygame.K_SPACE:
                if bullet_state is "ready":
                    # Get the current x cordinate of the spaceship
                    bulletX = playerX
                    fire_bullet(bulletX, bulletY)
                    bullet_change += 1



        if event.type == pygame.KEYUP:
            print('A keystroke has been released')
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT or event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                playerY_change = left_up_idle_movement
                playerX_change = right_down_idle_movement

    playerY += playerY_change
    playerX += playerX_change

    playerX += playerX_change
    if playerX <= 0:
        playerX = 0
    elif playerX >= 766:
        playerX = 766

    playerY += playerY_change
    if playerY <= 0:
        playerY = 0
    elif playerY >= 550:
        playerY = 550

    # Hostile Spyware Movement
    hostile_SpywareX += hostile_SpywareX_change
    if hostile_SpywareX <= 0:
        hostile_SpywareX_change = spyware_speed_right
        hostile_SpywareY += hostile_SpywareY_change
    elif hostile_SpywareX >= 766:
        hostile_SpywareX_change = spyware_speed_left

        hostile_SpywareY += hostile_SpywareY_change
        if hostile_SpywareY <= 0:
            hostile_SpywareY_change = 0.3
            hostile_SpywareY += hostile_SpywareY_change
        elif hostile_SpywareY >= 550:
            hostile_SpywareY = 550

        # Bullet Movement
    if bulletY <= 0:
        bulletY = 480
        bullet_state = "ready"

    if bullet_state is "fire":
        fire_bullet(bulletX, bulletY)
        bulletY -= bulletY_change

    player(playerX, playerY)
    # hostile
    hostile_spyware(hostile_SpywareX, hostile_SpywareY)
    pygame.display.update()
