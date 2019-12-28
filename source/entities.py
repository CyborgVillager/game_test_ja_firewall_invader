import pygame

playerX_location = 370
playerY_location = 500



# Player
player_Image = pygame.image.load('image/firewall_logo.png')
playerX = playerX_location
playerY = playerY_location
playerX_change = 0
playerY_change = 0
# user movement
left_up_player_speed = -0.1
right_down_player_speed = 0.1
# idle movement
left_up_idle_movement = -0
right_down_idle_movement = 0


hostile_SpywareX_Location = 370
hostile_SpywareY_Location = 650
hostile_Spyware_Change = 0

# Hostile Spyware
hostile_Spyware_Image = pygame.image.load('image/spyware0.png')
hostile_SpywareX = hostile_SpywareX_Location
hostile_SpywareY = hostile_SpywareY_Location
hostile_SpywareX_change = 0
hostile_SpywareY_change = 0
# user movement
left_up_hostile_spyware_speed = -0.1
right_down_hostile_spyware_speed = 0.1
# idle movement
left_up_idle_hostile_spyware_movement = -0
right_down_idle_hostile_spyware_movement = 0