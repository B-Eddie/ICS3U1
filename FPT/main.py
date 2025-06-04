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
GRAYBLUE = (83, 104, 114)
RED = (255, 0, 0)
GOLD = (255, 215, 0)

# music
fireSound = mixer.Sound("assets/sfx/flute.wav") #! remove comments to unmute
fireSound.play(loops=-1)

fart1 = mixer.Sound("assets/sfx/fart/1.wav")
fart2 = mixer.Sound("assets/sfx/fart/2.wav")
fart3 = mixer.Sound("assets/sfx/fart/3.wav")

pickup = mixer.Sound("assets/sfx/fart/pickup.wav")
damage = mixer.Sound("assets/sfx/die.wav")

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
score = 0
hearts = 3
mx, my = 0, 0
running = True
immunity = False
immunity_check = 0
boosts = []
max_poops = 10

# geese parts
poop_location = ""
geese_location = ""
goose_speed = 2
poop_chance = 0.01

# images
grass_background = image.load("assets/images/grass.png") # background image
heart = image.load("assets/images/heart.png")
background = image.load("assets/background.png")

player_x = width/2 - 50
player_y = height/2 - 50
player_speed = 5

player_rect = Rect(player_x + 15, player_y + 5, 70, 80)

player_movement = [False, False, False, False]

# Initialize screen
screen = display.set_mode((width, height))
display.set_caption("Geese S.H.E.E.T")


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
        draw.rect(screen, WHITE, blockValue) # draw button block
        draw.rect(screen, BLACK, blockValue, 3) # black border
        
        fontSize = neue_font.size(listTitle[i])
        
        # rectangle[2] is the width, setting the x value of where the text will start
        startX = (blockValue[2] - fontSize[0])//2 + blockValue[0] #centering the text over the width

        #rectangle[3] is the height, setting the y value of where the text will start
        startY = (blockValue[3] - fontSize[1])//2 + blockValue[1]
            
        #create this new rectangle, using the size as the width and height
        centeredRect = (startX, startY, fontSize[0], fontSize[1])


        # draw text in the buttons
        text = neue_font.render(listTitle[i], True, BLACK)
        screen.blit(text, centeredRect)
        
        if blockValue.collidepoint(mx,my):
            draw.rect(screen, GRAY, blockValue, 2) # draw the outline of the button block
            text = neue_font.render(listTitle[i], True, GRAYBLUE)
            screen.blit(text, centeredRect)

            if button == 1:
                currentState = stateList[i]

    title = neue_font_bold.render("Geese S.H.E.E.T", True, WHITE)
    screen.blit(title, (width/2 - title.get_width()/2, 50))
    
    return currentState
    
# function to draw geese
def drawGeese(screen, x, y, goose_image):
    goose = image.load("assets/images/geese/" + str(goose_image) + ".png")
    screen.blit(goose, (x, y))

# function to draw poop
def drawPoop(screen, x, y, poop_image):
    poop = image.load("assets/images/poop/" + str(poop_image) + ".png")
    screen.blit(poop, (x, y))

# function to remove poop from the screen + poop_location variable
def removePoop(x, y):
    global poop_location
    poop_location = poop_location.replace(str(x) + "," + str(y) + ",1", "") # try 3 times for different poop images
    poop_location = poop_location.replace(str(x) + "," + str(y) + ",2", "")
    poop_location = poop_location.replace(str(x) + "," + str(y) + ",3", "")

def drawBooster(screen):
    global boosts
    if boosts:
        boost = boosts[-1]
        color = ""
        # have different colors for different boosters
        if boost == "Immunity":
            color = GOLD
        elif boost == "Speed":
            color = GREEN

        text = neue_font_bold.render(str(boost), True, color)
        screen.blit(text, (width/2 - text.get_width()/2, 50))

def drawGame(screen):
    global player_x, player_y, player_rect, poop_location, geese_location, score, hearts, currentState, running, player_x, player_y, immunity, immunity_check


    current_time = time.get_ticks() # time

    # create collision for player
    player_rect = Rect(player_x + 15, player_y + 5, 70, 80)

    screen.blit(grass_background, (0, 0)) # draw background

    if immunity_check != 0:
        immunity_check -= 1
        draw.circle(screen, GOLD, (player_x + 50, player_y + 45), 50, 5)
        drawBooster(screen)
        if "Immunity" not in boosts:
            boosts.append("Immunity")
        if immunity_check == 0:
            immunity = False
            boosts.remove("Immunity")


    player_image = image.load("assets/images/character/1.png") # player image
    current_time = time.get_ticks() # get the current time
    animation_speed = 200  # milliseconds between animation frames
    
    if player_movement[0]: # w or up arrow
        if player_y > 0:
            player_y -= player_speed
        if current_time % animation_speed < animation_speed/2:
            player_image = image.load("assets/images/character/6.png")
        else:
            player_image = image.load("assets/images/character/5.png")
    if player_movement[1]: # s or down arrow
        if player_y < 600:
            player_y += player_speed
        if current_time % animation_speed < animation_speed/2:
            player_image = image.load("assets/images/character/2.png")
        else:
            player_image = image.load("assets/images/character/3.png")
    if player_movement[2]: # a or left arrow
        if player_x > 0:
            player_x -= player_speed
        if current_time % animation_speed < animation_speed/2:
            player_image = image.load("assets/images/character/9.png")
        else:
            player_image = image.load("assets/images/character/10.png")
    if player_movement[3]: # d or right arrow
        if player_x < 900:
            player_x += player_speed
        if current_time % animation_speed < animation_speed/2:
            player_image = image.load("assets/images/character/1.png")
        else:
            player_image = image.load("assets/images/character/4.png")

    # geese spawn and move
    # geese move randomly and poop sometimes spawns. unless the goose is 50px away from the player, then they get angry and move towards the player
    if geese_location == "":
        # initial geese spawn
        for i in range(random.randint(1, 3)): # number of geese spawning increase with difficulty
            if random.random() < 0.5:
                random_x = random.randint(100, 400)
            else:
                random_x = random.randint(700, 900)
            if random.random() < 0.5:
                random_y = random.randint(100, 300)
            else:
                random_y = random.randint(500, 600)

            geese_location += str(random_x) + "," + str(random_y) + ",1," + str(random.randrange(random_x - 50, random_x + 50, 10)) + "," + str(random.randrange(random_y - 50, random_y + 50, 10)) + ",0:" # x,y,goose_img,aim_x,aim_y,was_in_proximity:
    else:
        # update geese location
        for value in geese_location.split(":"):
            if value != "":
                vals = value.split(",")
                # x,y,goose_img,aim_x,aim_y,was_in_proximity:

                if int(vals[0]) == int(vals[3]) and int(vals[1]) == int(vals[4]): # if the target is reached
                    # generate new target values
                    # make sure the target is within the screen
                    if int(vals[3]) < 100:
                        vals[3] = str(int(vals[3]) + random.randrange(0, 50, 10))
                    elif int(vals[3]) > 800:
                        vals[3] = str(int(vals[3]) - random.randrange(0, 50, 10))
                    else:
                        vals[3] = str(int(vals[3]) + random.randrange(-50, 50, 10))

                    if int(vals[4]) < 100:
                        vals[4] = str(int(vals[4]) + random.randrange(0, 50, 10))
                    elif int(vals[4]) > 600:
                        vals[4] = str(int(vals[4]) - random.randrange(0, 50, 10))
                    else:
                        vals[4] = str(int(vals[4]) + random.randrange(-50, 50, 10))
                else: # if target isn't reached, tune values to move towards the target
                    # move towards the target
                    if int(vals[0]) < int(vals[3]): # x values
                        vals[0] = str(int(vals[0]) + random.randint(1, goose_speed))
                    elif int(vals[0]) > int(vals[3]):
                        vals[0] = str(int(vals[0]) - random.randint(1, goose_speed))
                    if int(vals[1]) < int(vals[4]): # y values
                        vals[1] = str(int(vals[1]) + random.randint(1, goose_speed))
                    elif int(vals[1]) > int(vals[4]):
                        vals[1] = str(int(vals[1]) - random.randint(1, goose_speed))

                # geese collision with player
                geese_rect = Rect(int(vals[0]) - 60, int(vals[1]) - 60, 220, 230)
                if player_rect.colliderect(geese_rect):
                    draw.rect(screen, RED, geese_rect, 1)
                    vals[3] = str(int(player_x))
                    vals[4] = str(int(player_y))
                    vals[5] = "1"  # if goose huge box colliding with player
                else:
                    if vals[5] == "1":  # if goose colliding box was touching player before
                        # get new target
                        vals[3] = str(int(vals[0]) + random.randrange(-50, 50, 10))
                        vals[4] = str(int(vals[1]) + random.randrange(-50, 50, 10))
                        vals[5] = "0"  # set proximity to not touching player
                
                # geese collision with player - losing hearts
                geese_rect_player = Rect(int(vals[0]) + 20, int(vals[1]) + 20, 70, 75)
                draw.rect(screen, RED, geese_rect_player, 1)
                if player_rect.colliderect(geese_rect_player) and not immunity:
                    damage.play()
                    hearts -= 1
                    player_x, player_y = 0, 0
                    if hearts == 0:
                        currentState = GAME_OVER
                    immunity = True
                    immunity_check = 200

                # goose randomly dropping poop
                # poop_chance
                if random.random() < poop_chance:
                    random_fart = random.randint(1, 3)
                    if random_fart == 1:
                        fart1.play()
                    elif random_fart == 2:
                        fart2.play()
                    else:
                        fart3.play()
                    poop_location += str(int(vals[0])) + "," + str(int(vals[1])) + "," + str(random_fart) + ":"


                # geese animation
                if current_time % 500 < 250:
                    vals[2] = 1
                else:
                    vals[2] = 2

                new_location = str(vals[0]) + "," + str(vals[1]) + "," + str(vals[2]) + "," + str(vals[3]) + "," + str(vals[4]) + "," + str(vals[5])
                geese_location = geese_location.replace(value, new_location)

    # check poop collision
    if poop_location:
        for value in poop_location.split(":"):
            if value != "":
                coord = value.split(",")
                poop_rect = Rect(int(coord[0]) + 20, int(coord[1]) + 55, 65, 45)
                if player_rect.colliderect(poop_rect):
                    pickup.play()
                    removePoop(int(coord[0]), int(coord[1]))
                    score += int(coord[2])
    # drow poop
    for i in poop_location.split(":"):
        if i != "":
            coord = i.split(",")
            drawPoop(screen, int(coord[0]), int(coord[1]), int(coord[2]))
    
    # draw geese
    for i in geese_location.split(":"):
        if i != "":
            coord = i.split(",")
            drawGeese(screen, int(coord[0]), int(coord[1]), int(coord[2]))



    # draw player
    screen.blit(player_image, (player_x, player_y))
    draw.rect(screen, RED, player_rect, 2) # player hitbox

    # draw hearts
    for i in range(hearts):
        screen.blit(heart, (180 + i * 30, 20))

    # draw score
    score_text = neue_font.render("Score: " + str(score), True, WHITE)
    screen.blit(score_text, (10, 10))

    # draw num poops
    total_poops = 0
    for i in poop_location.split(":"):
        if i != "":
            total_poops += 1

    poop_text = neue_font.render("Poops: " + str(total_poops) + "/" + str(max_poops), True, WHITE)
    screen.blit(poop_text, (10, 50))
    if total_poops >= max_poops:
        currentState = GAME_OVER

def drawInstructions(screen):
    screen.fill(BLACK)

def drawGameOver(screen):
    global score

    # text for game over
    game_over_text = neue_font_bold.render("Game Over", True, WHITE)
    score_text = neue_font.render("Score: " + str(score), True, WHITE) # score
    time_survived_text = neue_font.render("Time Survived: " + str(int(time_survived)) + "s", True, WHITE) # total time survived

    # text background
    draw.rect(screen, GRAY, (width/2 - time_survived_text.get_width()/2 - 10, height/2 - 50, time_survived_text.get_width() + 20, 200))

    # blit text to screen
    screen.blit(game_over_text, (width/2 - game_over_text.get_width()/2, height/2 - game_over_text.get_height()/2))
    screen.blit(score_text, (width/2 - score_text.get_width()/2, height/2 - score_text.get_height()/2 + 50))
    screen.blit(time_survived_text, (width/2 - time_survived_text.get_width()/2, height/2 - time_survived_text.get_height()/2 + 100))


# Game Loop
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
        if e.type == KEYDOWN:
            if e.key == 119 or e.key == 1073741906: # w or up arrow
                player_movement[0] = True
            elif e.key == 115 or e.key == 1073741905: # s or down arrow
                player_movement[1] = True
            elif e.key == 97 or e.key == 1073741904: # a or left arrow
                player_movement[2] = True
            elif e.key == 100 or e.key == 1073741903: # d or right arrow
                player_movement[3] = True
        if e.type == KEYUP:
            if e.key == 119 or e.key == 1073741906: # w or up arrow
                player_movement[0] = False
            elif e.key == 115 or e.key == 1073741905: # s or down arrow
                player_movement[1] = False
            elif e.key == 97 or e.key == 1073741904: # a or left arrow
                player_movement[2] = False
            elif e.key == 100 or e.key == 1073741903: # d or right arrow
                player_movement[3] = False

    
    # current state of the game
    if currentState == MENU:
        currentState = drawMenu(screen, mx, my, button, currentState)
    elif currentState == GAME:
        drawGame(screen)
        time_survived = time.get_ticks() / 1000
        
    elif currentState == INSTRUCTIONS:
        drawInstructions(screen)
    elif currentState == GAME_OVER:
        drawGameOver(screen)
    else:
        running = False

    display.flip()
    clock.tick(FPS)

quit()
