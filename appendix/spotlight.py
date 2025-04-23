import os
from pygame import * 


init()

size = width, height = 500, 600
screen = display.set_mode(size)

WHITE = (255, 255, 255)
YELLOW = (255, 255, 0)
BLUE = (0, 0, 255)

COLOR = YELLOW

screen.fill(WHITE)


running = True

# Game Loop
while running:
    for e in event.get():
        if e.type == QUIT:
            running = False
        if e.type == MOUSEMOTION:
            coord = e.pos
            screen.fill(WHITE)
            if coord[1] > 300:
                COLOR = BLUE
            else:
                COLOR = YELLOW
            draw.circle(screen, COLOR, coord, 30)
            display.flip()
    
quit()
