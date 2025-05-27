from pygame import *
import random

# initialize Pygame
init()

# Constants
FPS = 60
width = 1000
height = 700

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
BROWN = (139, 69, 19)
GRAY = (128, 128, 128)
RED = (255, 0, 0)

# Fonts
neue_font = font.Font("assets/fonts/neuebit-regular.otf", 40)
neue_font_bold = font.Font("assets/fonts/neuebit-bold.otf", 64)

# Game states
QUIT = 0
MENU = 1
GAME = 2
INSTRUCTIONS = 3
GAME_OVER = 4
currentState = MENU

# Game variables
score = 0
game_state = MENU
clock = time.Clock()

# Initialize screen
screen = display.set_mode((width, height))
display.set_caption("Geese Defenders")

background = image.load("assets/background.png")

def drawMenu(screen, mx, my, button, currentState):
    screen.fill(GRAY)
    screen.blit(background, (0, 0, 100, 70))

    x = width / 3; y1 = 200; y2 = 350; y3 = 500
    blockW = 300; blockH = 100
    
    stateList = [GAME, INSTRUCTIONS, QUIT]
    listTitle = ["Play", "Instructions", "Quit"]
    blockList = [Rect(x, y1, blockW, blockH),
        Rect(x, y2, blockW, blockH),
        Rect(x, y3, blockW, blockH)]
    
    for i in range(len(blockList)):
        blockValue = blockList[i]
        draw.rect(screen, BLACK, blockValue) # draw button block
        
        # draw text in the buttons
        text = neue_font.render(listTitle[i], True, WHITE)
        screen.blit(text, (blockValue.x + 10, blockValue.y + 25))

        if blockValue.collidepoint(mx,my):
            draw.rect(screen, GRAY, blockValue, 2) # draw the outline of the button block

            if button == 1:
                currentState = stateList[i]

    title = neue_font_bold.render("Geese Defenders", True, WHITE)
    screen.blit(title, (width/2 - title.get_width()/2, 50))
    
    return currentState
    
def drawGame(screen):
    screen.fill(GREEN)

def drawInstructions(screen):
    screen.fill(BLACK)

# Game Loop
mx, my = 0, 0
running = True
while running:
    button = 0

    for e in event.get():
        if e.type == QUIT:
            running = False
        
        if e.type == MOUSEBUTTONDOWN:
            mx, my = e.pos                             
            button = e.button
        if e.type == MOUSEMOTION:
            mx, my = e.pos

    if currentState == MENU:
        currentState = drawMenu(screen, mx, my, button, currentState)
    elif currentState == GAME:
        drawGame(screen)
    elif currentState == INSTRUCTIONS:
        drawInstructions(screen)
    else:
        running = False

    display.flip()
    clock.tick(FPS)

quit()
