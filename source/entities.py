import pygame
import random



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


hostile_Spyware_Image = []
hostile_SpywareX_Location = []
hostile_SpywareY_Location = []
hostile_Spyware_health = []
spyware_speed_right = []
spyware_speed_left = []
hostile_SpywareX_change = []
hostile_SpywareY_change = []
number_of_hostiles = 63




# Hostile Spyware
for i in range(number_of_hostiles):
    hostile_Spyware_Image.append(pygame.image.load('image/spyware0.png'))
    hostile_SpywareX_Location.append(random.randint(0,735))
    hostile_SpywareY_Location.append(random.randint(0,30))
    hostile_Spyware_health.append(2)
    spyware_speed_right.append(2)
    spyware_speed_left.append(-2)
    hostile_SpywareX_change.append(2)
    # move down by 15 pixels
    hostile_SpywareY_change.append(35)

hostile_SpywareY_Location += hostile_SpywareY_change
hostile_SpywareX_Location += hostile_SpywareX_change




