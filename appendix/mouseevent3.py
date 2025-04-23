import os
from pygame import * 


init()

size = width, height = 800, 600
screen = display.set_mode(size)
button = 0

BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
BLUE = (0, 0, 255)

COLOR = WHITE

SIZE = 1

def drawScene(screen):
    mx, my = mouse.get_pos()
    draw.circle(screen, COLOR, (mx,my), SIZE)
    
    display.flip()

draw.rect(screen, GREEN, (0, 0, 400, 100)) # fill the screen with black
draw.rect(screen, WHITE, (400, 0, 800, 100)) # fill the top left with white
draw.rect(screen, BLUE, (0, 100, 100, 40)) # fill the bottom with black
draw.rect(screen, RED, (100, 100, 100, 40)) # fill the bottom with black
display.flip()

running = True

# Game Loop
while running:
    for e in event.get():             # checks all events that happen
        if e.type == QUIT:
            running = False
        if e.type == MOUSEBUTTONDOWN:
            button = e.button
            coord = e.pos
            print(coord)
            if coord[0] < 400 and coord[1] < 100:
                COLOR = GREEN
            elif coord[0] > 400 and coord[1] < 100:
                COLOR = WHITE
            elif coord[0] > 0 and coord[0] < 100 and coord[1] > 100 and coord[1] < 140:
                SIZE -= 1
            elif coord[0] > 100 and coord[0] < 200 and coord[1] > 100 and coord[1] < 140:
                SIZE += 1
            else:
                drawScene(screen)
            
    
quit()
