import pygame

pygame.init()

SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 1000

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

# player
player = pygame.Rect((SCREEN_WIDTH/2), (SCREEN_HEIGHT/2), 50, 50)

# player variables
player_xvel = player_yvel = 0
player_left = player_right = player_up = player_down = 0

# smooth movement
def movement_phys(speed, friction):
    # global variables because python
    global player_xvel, player_yvel
    global player_left, player_right, player_up, player_down
    
    player_xvel += (player_right + (0 - player_left)) * speed
    player_xvel = player_xvel * friction
    
    player_yvel += (player_down + (0 - player_up)) * speed
    player_yvel = player_yvel * friction

clock = pygame.time.Clock()

run = True
while run:
    clock.tick(60)  # cap to 60 FPS for consistency
    screen.fill((0, 0, 0))

    pygame.draw.rect(screen, (255, 255, 255), player)

    key = pygame.key.get_pressed()
    
    # update directional inputs
    player_left = key[pygame.K_a]
    player_right = key[pygame.K_d]
    player_up = key[pygame.K_w]
    player_down = key[pygame.K_s]

    movement_phys(3, 0.9)
    player.move_ip(player_xvel, player_yvel)

    # event handler
    for event in pygame.event.get():
        if event.type == pygame.QUIT or key[pygame.K_ESCAPE] == True:
            run = False
    
    # updates the screen
    pygame.display.update()

pygame.quit()