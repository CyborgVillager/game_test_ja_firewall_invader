# only right side side go down, left has to loop back to right
"""""
# Hostile Spyware
hostile_Spyware_Image = pygame.image.load('image/spyware0.png')
hostile_SpywareX_Location = random.randint(0,800)
hostile_SpywareY_Location = random.randint(0,30)

hostile_SpywareX = hostile_SpywareX_Location
hostile_SpywareY = hostile_SpywareY_Location
spyware_speed_right =.05
spyware_speed_left = -.06
hostile_SpywareX_change = 0.3
# move down by 15 pixels
hostile_SpywareY_change = 15


hostile_SpywareY += hostile_SpywareY_change
hostile_SpywareX += hostile_SpywareX_change


# Hostile Spyware Movement
hostile_SpywareX += hostile_SpywareX_change
if hostile_SpywareX <= 0:
    hostile_SpywareX_change = spyware_speed_right
elif hostile_SpywareX >= 766:
    hostile_SpywareX_change = spyware_speed_left

    hostile_SpywareY += hostile_SpywareY_change
    if hostile_SpywareY <= 0:
        hostile_SpywareY_change = 0
    elif hostile_SpywareY >= 550:
        hostile_SpywareY = 550
        
"""""
