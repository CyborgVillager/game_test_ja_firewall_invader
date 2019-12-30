import pygame
import math
from entities import *

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
player_bullet_destroyed_hostile_score = 0
font = pygame.font.Font('freesansbold.ttf', 32)

textX = 10
testY = 10

# Game Over
over_font = pygame.font.Font('freesansbold.ttf', 64)


# Player
def player(x, y):  # new values for x & y are able to be drawn on the screen
    # draw the player onto the screen
    window_screen.blit(player_Image, (x, y))


def fire_bullet(x, y):
    global bullet_state
    bullet_state = "fire"
    window_screen.blit(bullet_Image, (x, y + 40))


def isCollision(hostile_SpywareX_Location, hostile_SpywareY_Location , bulletX_Location, bulletY_Location):
    distance = math.sqrt(math.pow(hostile_SpywareX_Location - bulletX_Location, 2) + (math.pow(hostile_SpywareY_Location - bulletY_Location, 2)))
    if distance < 27 :
        return True
    else:
        return False


# Hostile Types
def hostile_Spyware(x, y,i):  # new values for x & y are able to be drawn on the screen
    # draw the player onto the screen
    window_screen.blit(hostile_Spyware_Image[i], (x, y))


# Game Loop
running = True
while running:
    # Has red,green, blue
    window_screen.fill((0, 0, 0))
    # Background Image
    window_screen.blit(background, (0, 0))

    # keystrokes
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        # sys will check if keystroke is pressed by user
        if event.type == pygame.KEYDOWN:
            # print('A keystroke has been pressed')
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
                    bulletX_Location = playerX
                    fire_bullet(bulletX_Location, bulletY_Location)

        if event.type == pygame.KEYUP:
            # print('A keystroke has been released')
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
    for i in range(number_of_hostiles):
        hostile_SpywareX_Location[i] += hostile_SpywareX_change[i]
        if hostile_SpywareX_Location[i] <= 0:
            hostile_SpywareX_change[i] = spyware_speed_right[i]
            hostile_SpywareY_Location[i] += hostile_SpywareY_change[i]
        elif hostile_SpywareX_Location[i] >= 766:
            hostile_SpywareX_change[i] = spyware_speed_left[i]

            hostile_SpywareY_Location[i] += hostile_SpywareY_change[i]
            if hostile_SpywareY_Location[i] <= 0:
                hostile_SpywareY_change[i] = 0.3
                hostile_SpywareY_Location[i] += hostile_SpywareY_change[i]
            elif hostile_SpywareY_Location[i] >= 550:
                hostile_SpywareY_Location[i] = 550

            # Collision
        collision = isCollision(hostile_SpywareX_Location[i], hostile_SpywareY_Location[i], bulletX_Location, bulletY_Location)
        if collision:
            bulletY_Location = 480
            bullet_state = "ready"
            player_bullet_destroyed_hostile_score += 1
            print(player_bullet_destroyed_hostile_score)
            hostile_SpywareX_Location[i] = random.randint(0, 736)
            hostile_SpywareY_Location[i] = random.randint(50, 150)

        hostile_Spyware(hostile_SpywareX_Location[i], hostile_SpywareY_Location[i],i)

        # Bullet Movement
    if bulletY_Location <= 0:
        bulletY_Location = playerY
        bullet_state = "ready"

    if bullet_state is "fire":
        fire_bullet(bulletX_Location, bulletY_Location)
        bulletY_Location -= bulletY_change

    if bulletY_Location <= 0:
        bulletY_Location = playerY
        bullet_state = "ready"



    # Enemy Movement

    player(playerX, playerY)

    pygame.display.update()
