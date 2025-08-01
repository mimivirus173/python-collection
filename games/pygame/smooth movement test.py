import pygame as pg

pg.init()

SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 1000

screen = pg.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

# player
player = pg.Rect((SCREEN_WIDTH/2), (SCREEN_HEIGHT/2), 50, 50)

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

clock = pg.time.Clock()

run = True
while run:
    clock.tick(60)  # cap to 60 FPS for consistency
    screen.fill((0, 0, 0))

    pg.draw.rect(screen, (255, 255, 255), player)

    key = pg.key.get_pressed()
    
    # update directional inputs
    player_left = key[pg.K_a] or key[pg.K_LEFT]
    player_right = key[pg.K_d] or key[pg.K_RIGHT]
    player_up = key[pg.K_w] or key[pg.K_UP]
    player_down = key[pg.K_s] or key[pg.K_DOWN]

    movement_phys(3, 0.9)
    player.move_ip(player_xvel, player_yvel)

    # event handler
    for event in pg.event.get():
        if event.type == pg.QUIT or key[pg.K_ESCAPE] == True:
            run = False
    
    # updates the screen
    pg.display.update()

pg.quit()