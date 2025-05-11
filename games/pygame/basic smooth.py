import pygame

pygame.init()

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 800

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

player = pygame.Rect(400, 400, 50, 50)

run = True
while run:
    # fills the screen with black at the start of the loop i.e. refreshes the screen
    screen.fill((0, 0, 0))
    
    # draws the player on the screen
    pygame.draw.rect(screen, (0, 255, 0), player)

    key = pygame.key.get_pressed()
    
    # movement
    if key[pygame.K_a] == True: player.move_ip(-1, 0)
    elif key[pygame.K_d] == True: player.move_ip(1, 0)
    elif key[pygame.K_w] == True: player.move_ip(0, -1)
    elif key[pygame.K_s] == True: player.move_ip(0, 1)

    # event handler
    for event in pygame.event.get():
        if event.type == pygame.QUIT or key[pygame.K_ESCAPE] == True:
            run = False
    
    # updates the screen
    pygame.display.update()

pygame.quit()