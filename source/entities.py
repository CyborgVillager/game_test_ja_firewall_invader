import pygame
import random
from random import randint


playerX_location = 370
playerY_location = 500



# Player
player_Image = pygame.image.load('image/firewall_logo.png')
playerX = playerX_location
playerY = playerY_location
playerX_change = 0
playerY_change = 0
# user movement
left_up_player_speed = -2
right_down_player_speed = 2
# idle movement
left_up_idle_movement = -0
right_down_idle_movement = 0

# Bullet
bullet_Image = pygame.image.load('image/zero_bullet.png')
bulletX_Location = 0
bulletY_Location = 480
bulletX_change = 0
bulletY_change = 10
bullet_state = "ready"
player_bullet_destroyed_hostile_score = 0



# Hostile Spyware
hostile_Spyware_Image = []
hostile_SpywareX_Location = []
hostile_SpywareY_Location = []
hostile_SpywareX = []
hostile_SpywareY = []
hostile_SpywareX_change = []
hostile_SpywareY_change = []
number_of_hostiles = 10




for i in range(number_of_hostiles):
    hostile_Spyware_Image.append(pygame.image.load('image/spyware0.png'))
    hostile_SpywareX_Location.append(random.randint(0,735))
    hostile_SpywareY_Location.append(random.randint(0,30))
    spyware_speed_right =1
    spyware_speed_left = -1
    hostile_SpywareX_change = 0.3
    # move down by 15 pixels
    hostile_SpywareY_change = 15






