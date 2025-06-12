from pygame import *

init()
size = width, height = 1000,700
screen = display.set_mode(size)

WHITE = (225,225,225)
BLACK = (0, 0, 0)
REDDISH = (180, 101, 74)
GRAY = (194, 197, 187)
GREEN = (73, 159, 104)
LIGHT_GREEN = (119, 178, 140)
CYAN_GREEN = (21, 122, 110)

STATE_MENU = 0
STATE_GAME = 1
STATE_HELP = 2
STATE_QUIT = 3
STATE_LVL1 = 4
STATE_LVL2 = 5
STATE_LVL3 = 6
myFont = font.SysFont("Times New Roman",30)

#loading images

#Images for the menu
forestmenu = image.load("forest_pix.jpg")
forestmenu = transform.scale(forestmenu, (width, height)) #fullscales the image
stages = image.load("stages.jpg")
stages = transform.scale(stages, (width, height))
menu1 = image.load("menu_button.png")
menu1 = transform.scale(menu1, (450,230))
pin = image.load("pindrop.png")
pin = transform.scale(pin, (170,170))

#Images for the first level
forestlvl = image.load("forestt.png")
forestlvl = transform.scale(forestlvl, (width+200, height))

#Images for Level 2
seapic = image.load("sea.png")
seapic = transform.scale(seapic, (width, height))

#Trash items
can_img = image.load("pepsican.png")
can_img = transform.scale(can_img, (60, 60))
sodarings = image.load("sodarings.png")
sodarings = transform.scale(sodarings, (50,80))
bag = image.load("bag.png")
bag = transform.scale(bag, (60, 60))

item_images = [can_img, bag, sodarings]
item_rects = [Rect(200, 300, 60, 60), Rect(400, 200, 60, 60), Rect(200,300,50,80)]
item_drags = [False, False]
trash_rect = Rect(850, 550, 120, 120)

lvl1 = screen.blit(pin, (40,300))
lvl2 = screen.blit(pin, (300,190))
lvl3 = screen.blit(pin, (540,430))

can_drag = False
bag_drag = False
soda_drag = False
can_rect = Rect(200,300,60,60)
bag_rect = Rect(200,300,60,60)
soda_rect = Rect(200,300,50,80)
    

def drawMenu(mx, my, button, currentState):
    x = 550; y1 = 50; y2 = 250; y3 = 450;
    blockW = 450; blockH = 230
    
    rect1 = Rect(x, y1, blockW, blockH)
    rect2 = Rect(x, y2, blockW, blockH)
    rect3 = Rect(x, y3, blockW, blockH)
    
    text1 = myFont.render("PLAY GAME", 1, WHITE)
    text2 = myFont.render("HELP", 1, WHITE)
    text3 = myFont.render("QUIT", 1, WHITE)
    
    text1Width, text1Height = myFont.size("PLAY GAME")
    text2Width, text2Height = myFont.size("HELP")
    text3Width, text3Height = myFont.size("QUIT")    
    
    text_X1_Value = x + (blockW - text1Width)//2.2
    text_Y1_Value = y1 + (blockH - text1Height)//2
    text_X2_Value = x + (blockW - text2Width)//2.2
    text_Y2_Value = y2 + (blockH - text2Height)//2     
    text_X3_Value = x + (blockW - text3Width)//2.2
    text_Y3_Value = y3 + (blockH - text3Height)//2
    
    screen.blit(forestmenu, (0,0))
    
    screen.blit(menu1, (rect1))
    screen.blit(menu1, (rect2))
    screen.blit(menu1, (rect3))
    '''
    draw.rect(screen, GRAY, rect1) 
    draw.rect(screen, GRAY, rect2) 
    draw.rect(screen, GRAY, rect3)
    '''
    
    screen.blit(text1, (text_X1_Value,text_Y1_Value,text1Width, text1Height))
    screen.blit(text2, (text_X2_Value,text_Y2_Value,text2Width, text2Height))
    screen.blit(text3, (text_X3_Value,text_Y3_Value,text3Width, text3Height))
    
    
    
    if button == 1:
        if rect1.collidepoint(mx,my):
            currentState = STATE_GAME
        elif rect2.collidepoint(mx,my):
            currentState = STATE_HELP
        elif rect3.collidepoint(mx,my):
            currentState = STATE_QUIT
    return currentState
    
     
def drawGame(mx, my, button, currentState, backx):
    screen.blit(stages, (0, 0))

    # Draw the level selection pins
    lvl1_rect = screen.blit(pin, (40, 300))     # Pin for Level 1
    lvl2_rect = screen.blit(pin, (300, 190))    # Pin for Level 2
    lvl3_rect = screen.blit(pin, (540, 430))    # Pin for Level 3

    # Handle input
    if button == 1:  # Left click
        if lvl1_rect.collidepoint(mx, my):
            return STATE_LVL1, backx
        elif lvl2_rect.collidepoint(mx, my):
            return STATE_LVL2, backx
        elif lvl3_rect.collidepoint(mx, my):
            return STATE_LVL3, backx

    elif button == 3:  # Right click
        return STATE_MENU, backx

    return currentState, backx
        
    if button == 3:
        currentState = STATE_MENU
    return currentState, backx

def drawLvl1(mx, my, button, mouse_pressed, currentState, backx):
    global can_drag, bag_drag, soda_drag, offset_x, offset_y
    
    screen.blit(forestlvl, (0, 0))
    label = myFont.render("Level 1 - Right click to return", True, WHITE)
    # Draw trash bin
    draw.rect(screen, GRAY, trash_rect)

    # Handle can dragging
    if button == 1 and can_rect.collidepoint(mx, my) and not bag_drag:  # Start dragging can
        print("Starting can drag")
        can_drag = True
        offset_x = mx - can_rect.x
        offset_y = my - can_rect.y
    elif not mouse_pressed and can_drag:  # Stop dragging can when mouse is released
        print("Stopping can drag")
        can_drag = False
        # Check if can is in trash
        if can_rect.colliderect(trash_rect):
            can_rect.x = -1000
            can_rect.y = -1000

    # Handle bag dragging
    if button == 1 and bag_rect.collidepoint(mx, my) and not can_drag:  # Start dragging bag
        print("Starting bag drag")
        bag_drag = True
        offset_x = mx - bag_rect.x
        offset_y = my - bag_rect.y
    elif not mouse_pressed and bag_drag:  # Stop dragging bag when mouse is released
        print("Stopping bag drag")
        bag_drag = False
        # Check if bag is in trash
        if bag_rect.colliderect(trash_rect):
            bag_rect.x = -1000
            bag_rect.y = -1000
            
    if button == 1 and soda_rect.collidepoint(mx, my) and not can_drag and not bag_drag:  # Start dragging soda rings
        print("Starting bag drag")
        soda_drag = True
        offset_x = mx - soda_rect.x
        offset_y = my - soda_rect.y
    elif not mouse_pressed and soda_drag:  # Stop dragging bag when mouse is released
        print("Stopping soda drag")
        soda_drag = False
        # Check if bag is in trash
        if soda_rect.colliderect(trash_rect):
            soda_rect.x = -1000
            soda_rect.y = -1000

    # Update positions while dragging
    if can_drag and mouse_pressed:
        new_x = mx - offset_x
        new_y = my - offset_y
        print(f"Dragging can to ({new_x}, {new_y})")
        can_rect.x = new_x
        can_rect.y = new_y
    if bag_drag and mouse_pressed:
        new_x = mx - offset_x
        new_y = my - offset_y
        print(f"Dragging bag to ({new_x}, {new_y})")
        bag_rect.x = new_x
        bag_rect.y = new_y
    if soda_drag and mouse_pressed:
        new_x = mx - offset_x
        new_y = my - offset_y
        print(f"Dragging soda to ({new_x}, {new_y})")
        soda_rect.x = new_x
        soda_rect.y = new_y

    # Draw items after updating positions
    screen.blit(can_img, can_rect)
    screen.blit(bag, bag_rect)
    screen.blit(sodarings, soda_rect)

    screen.blit(label, (50, 50))
    if button == 3:
        return STATE_GAME, backx
    return currentState, backx

def drawLvl2(mx, my, button, currentState, backx):
    screen.blit(seapic, (backx, 0))
    screen.blit(seapic, (backx + width, 0))

    backx -= 1  # Move the background to the left

    if backx <= -width:
        backx = 0  # Reset the scroll

    label = myFont.render("Level 2 - Right click to return", True, WHITE)
    screen.blit(label, (50, 50))

    if button == 3:
        return STATE_GAME, backx
    return currentState, backx

    
def drawHelp(mx, my, button, currentState):
    
    if button == 3:
        currentState = STATE_MENU
    return currentState    


currentState = STATE_MENU
mx = my = 0                              
running = True
backgroundx = 0

# Game Loop
while running:

    button = 0
    mouse_pressed = mouse.get_pressed()[0]
    for e in event.get():
        if e.type == QUIT:
            running = False
        if e.type == MOUSEBUTTONDOWN:
            mx, my = e.pos                             
            button = e.button
        if e.type == MOUSEMOTION:
            mx, my = e.pos
            
    if currentState == STATE_MENU:
        currentState = drawMenu(mx, my, button,currentState)

    elif currentState == STATE_GAME:
        currentState, backgroundx = drawGame(mx, my, button, currentState, backgroundx)
        
    elif currentState == STATE_LVL1:
        currentState, backgroundx = drawLvl1(mx, my, button, mouse_pressed, currentState, backgroundx)
    
    elif currentState == STATE_LVL2:
        currentState, backgroundx = drawLvl2(mx, my, button, currentState, backgroundx)
        
    elif currentState == STATE_LVL3:
        currentState, backgroundx = drawLvl3(mx, my, button, currentState, backgroundx)

        
    elif currentState == STATE_HELP:
        currentState = drawHelp(mx, my, button, currentState)
    
    else:
        running = False
        
    display.update()

                              
quit()
