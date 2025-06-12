# Name: Eddie Bian
# Date: May 12, 2025
# Course Code: ICS3U1
# Description: FPT

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
fireSound = mixer.Sound("assets/sfx/flute.wav")
fireSound.play(loops=-1)

fart1 = mixer.Sound("assets/sfx/fart/1.wav")
fart2 = mixer.Sound("assets/sfx/fart/2.wav")
fart3 = mixer.Sound("assets/sfx/fart/3.wav")

pickup = mixer.Sound("assets/sfx/fart/pickup.wav")
damage = mixer.Sound("assets/sfx/die.wav")

# Fonts
neue_font = font.Font("assets/fonts/neuebit-regular.otf", 40)
neue_font_bold = font.Font("assets/fonts/neuebit-bold.otf", 64)
small_neue_font = font.Font("assets/fonts/neuebit-regular.otf", 20)

# Game states
QUIT = 0
MENU = 1
GAME = 2
INSTRUCTIONS = 3
LEADERBOARD = 4
GAME_OVER = 5
NAME_ENTRY = 6
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
speed_boost = False
speed_boost_check = 100
boosts = []
max_poops = 20
mute_button = False
restart = False
maxgeese = 2
level = 1
last_level_increase = 0
booster_chance = 0.001
player_name = ""
entering_name = False
goose_id_counter = 0

# geese parts
poop_location = ""
boost_location = ""
geese_location = ""
goose_speed = 2
poop_chance = 0.01

# images
grass_background = image.load("assets/images/grass.png") # background image
heart = image.load("assets/images/heart.png")
background = image.load("assets/background.png")
mute_icon = image.load("assets/images/mute.png")
unmute_icon = image.load("assets/images/unmute.png")

# player variables
player_x = width/2 - 50
player_y = height/2 - 50
player_speed = 5
player_rect = Rect(player_x + 15, player_y + 5, 70, 80)
player_movement = [False, False, False, False] # [w, s, a, d] movement keys

# Initialize screen
screen = display.set_mode((width, height))
display.set_caption("Geese S.H.E.E.T")

# draw menu function
def drawMenu(screen, mx, my, button, currentState):
    global mute_button, mute_icon, unmute_icon

    # background 
    screen.fill(GRAY)
    screen.blit(background, (0, 0, 100, 70))

    # variables for button blocks
    x = width / 3; y1 = 150; y2 = 270; y3 = 390; y4 = 510
    blockW = 300; blockH = 100
    
    # note: code from teacher
    stateList = [GAME, INSTRUCTIONS, LEADERBOARD, QUIT]
    listTitle = ["Play", "Instructions", "Leaderboard", "Quit"]
    blockList = [Rect(x, y1, blockW, blockH),
        Rect(x, y2, blockW, blockH),
        Rect(x, y3, blockW, blockH),
        Rect(x, y4, blockW, blockH)]
    
    # loop through the button blocks and draw them
    for button_index in range(len(blockList)):
        blockValue = blockList[button_index]
        draw.rect(screen, WHITE, blockValue) # draw button block
        draw.rect(screen, BLACK, blockValue, 3) # black border
        
        fontSize = neue_font.size(listTitle[button_index])
        
        # rectangle[2] is the width, setting the x value of where the text will start
        startX = (blockValue[2] - fontSize[0])//2 + blockValue[0] #centering the text over the width

        #rectangle[3] is the height, setting the y value of where the text will start
        startY = (blockValue[3] - fontSize[1])//2 + blockValue[1]
            
        #create this new rectangle, using the size as the width and height
        centeredRect = (startX, startY, fontSize[0], fontSize[1])

        # draw text in the buttons
        text = neue_font.render(listTitle[button_index], True, BLACK)
        screen.blit(text, centeredRect)
        
        # if user clicks on the button
        if blockValue.collidepoint(mx,my):
            draw.rect(screen, GRAY, blockValue, 2) # draw the outline of the button block
            text = neue_font.render(listTitle[button_index], True, GRAYBLUE)
            screen.blit(text, centeredRect)

            if button == 1:
                currentState = stateList[button_index]

    # Draw mute button
    # resize images
    mute_icon = transform.scale(mute_icon, (30, 30))
    unmute_icon = transform.scale(unmute_icon, (30, 30))

    mute_button_rect = Rect(width - 100, 20, 50, 50)
    draw.rect(screen, WHITE, mute_button_rect)
    draw.rect(screen, BLACK, mute_button_rect, 2)
    if mute_button:
        screen.blit(mute_icon, (width - 100 + 10, 20 + 10))
    else:
        screen.blit(unmute_icon, (width - 100 + 10, 20 + 10))
        # make image smaller

    # mute button colliding with mouse
    if mute_button_rect.collidepoint(mx, my):
        draw.rect(screen, GRAY, mute_button_rect, 2)

        if button == 1: # able to be toggled
            if not mute_button:
                mixer.pause()
                mute_button = True
            else:
                mixer.unpause()
                mute_button = False

    # draw title
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

    # remove poop from the poop_location variable
    poop_location = poop_location.replace(str(x) + "," + str(y) + ",1", "") # try 3 times for different poop images
    poop_location = poop_location.replace(str(x) + "," + str(y) + ",2", "")
    poop_location = poop_location.replace(str(x) + "," + str(y) + ",3", "")
    poop_location = poop_location.replace("::", ":") # remove duplicates left behind from removing the values in between

# draw boosters
def drawBoosterImage(screen, x, y, booster_type):
    booster = image.load("assets/images/boosters/" + str(booster_type.lower()) + ".png")
    screen.blit(booster, (x, y))

# remove booster x y value from the boost_location variable
def removeBooster(x, y):
    global boost_location
    boost_location = boost_location.replace(str(x) + "," + str(y) + ",Immunity", "")
    boost_location = boost_location.replace(str(x) + "," + str(y) + ",Speed", "")

# draw booster text on top of the screen
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

# main game function
def drawGame(screen):
    global player_x, player_y, player_rect, poop_location, geese_location, score, hearts, currentState, running, player_x, player_y, immunity, immunity_check, mute_button, level, last_level_increase, goose_speed, maxgeese, poop_chance, max_poops, boost_location, boost_type, boosts, player_speed, goose_id_counter, speed_boost, speed_boost_check

    # time for animations, time survived, and level increase
    current_time = time.get_ticks()

    # difficulty increase
    if current_time - last_level_increase >= 10000:  # every 10 seconds
        level += 1
        last_level_increase = current_time
        # change difficulty variables
        # goose speed up to max of 5
        if goose_speed + 0.5 < 5:
            goose_speed += 0.5
        else:
            goose_speed = 5  
            
        # geese spawn every 20 seconds
        geese_location += str(goose_id_counter + 1) + "," + str(random.randint(100, 900)) + "," + str(random.randint(100, 600)) + ",1," + str(random.randrange(100, 900, 10)) + "," + str(random.randrange(100, 600, 10)) + ",0:" # id,x,y,goose_img,aim_x,aim_y,was_in_proximity:
        
            
        # increase poop chance up to 5%
        if poop_chance + 0.005 < 0.05:
            poop_chance += 0.005
        else:
            poop_chance = 0.05

        # decrease max poops
        max_poops += 1


    # create collision for player
    player_rect = Rect(player_x + 15, player_y + 5, 70, 80)

    screen.blit(grass_background, (0, 0)) # draw background

    # draw immune circle if player is immune
    if immunity_check != 0:
        immunity_check -= 1
        draw.circle(screen, GOLD, (player_x + 50, player_y + 45), 50, 5)
        drawBooster(screen)
        if "Immunity" not in boosts:
            boosts.append("Immunity")
        if immunity_check == 0:
            immunity = False
            boosts.remove("Immunity")

    # speed boost
    if speed_boost:
        speed_boost_check -= 1
        if speed_boost_check == 0:
            speed_boost = False
            player_speed = 5
            if player_speed < player_speed:
                player_speed = player_speed

    # player movement
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

    #! Drawing all the objects
    # check poop collision
    if poop_location:
        for value in poop_location.split(":"):
            if value != "":
                coord = value.split(",")
                poop_rect = Rect(int(coord[0]) + 20, int(coord[1]) + 55, 65, 45)
                if player_rect.colliderect(poop_rect):
                    if not mute_button:
                        pickup.play()
                    removePoop(int(coord[0]), int(coord[1]))
                    score += int(coord[2])
    
    # draw poop
    for poop in poop_location.split(":"):
        if poop != "":
            coord = poop.split(",")
            drawPoop(screen, int(coord[0]), int(coord[1]), int(coord[2]))

    # draw booster
    for boost in boost_location.split(":"):
        if boost != "":
            coord = boost.split(",")
            # draw booster
            drawBoosterImage(screen, int(coord[0]), int(coord[1]), coord[2])
            
    # draw geese
    for values in geese_location.split(":"):
        if values != "":
            coord = values.split(",")
            drawGeese(screen, int(coord[1]), int(coord[2]), int(coord[3]))

    # geese spawn and move
    if geese_location == "":
        # initial geese spawn
        for i in range(random.randint(1, int(maxgeese))): # random number of geese initially spawning
            if random.random() < 0.5:
                random_x = random.randint(100, 400)
            else:
                random_x = random.randint(700, 900)
            if random.random() < 0.5:
                random_y = random.randint(100, 300)
            else:
                random_y = random.randint(500, 600)

            goose_id_counter += 1 # geese id for tracking
            geese_location += str(goose_id_counter) + "," + str(random_x) + "," + str(random_y) + ",1," + str(random.randrange(random_x - 50, random_x + 50, 10)) + "," + str(random.randrange(random_y - 50, random_y + 50, 10)) + ",0:" # id,x,y,goose_img,aim_x,aim_y,was_in_proximity:
    else:
        # update geese location
        new_geese_location = ""
        for value in geese_location.split(":"):
            if value != "":
                vals = value.split(",")
                # id,x,y,goose_img,aim_x,aim_y,was_in_proximity:

                if int(vals[1]) == int(vals[4]) and int(vals[2]) == int(vals[5]): # if the target is reached
                    # generate new target values
                    # make sure the target is within the screen
                    if int(vals[4]) < 100:
                        vals[4] = str(int(vals[4]) + random.randrange(0, 80, 10))
                    elif int(vals[4]) > 800:
                        vals[4] = str(int(vals[4]) - random.randrange(0, 80, 10))
                    else:
                        vals[4] = str(int(vals[4]) + random.randrange(-80, 80, 10))

                    if int(vals[5]) < 100:
                        vals[5] = str(int(vals[5]) + random.randrange(0, 80, 10))
                    elif int(vals[5]) > 600:
                        vals[5] = str(int(vals[5]) - random.randrange(0, 80, 10))
                    else:
                        vals[5] = str(int(vals[5]) + random.randrange(-80, 80, 10))
                else: # if target isn't reached, tune values to move towards the target
                    # move towards the target
                    if int(vals[1]) < int(vals[4]): # x values
                        vals[1] = str(int(vals[1]) + random.randint(1, int(goose_speed)))
                    elif int(vals[1]) > int(vals[4]):
                        vals[1] = str(int(vals[1]) - random.randint(1, int(goose_speed)))
                    if int(vals[2]) < int(vals[5]): # y values
                        vals[2] = str(int(vals[2]) + random.randint(1, int(goose_speed)))
                    elif int(vals[2]) > int(vals[5]):
                        vals[2] = str(int(vals[2]) - random.randint(1, int(goose_speed)))

            
                # geese collision with player
                geese_rect = Rect(int(vals[1]) - 60, int(vals[2]) - 60, 220, 230)
                if player_rect.colliderect(geese_rect):
                    # determine direction of goose to draw red eyes
                    if int(vals[1]) < int(vals[4]): # right
                        draw.circle(screen, RED, (int(vals[1]) + 65, int(vals[2]) + 30), 5)
                    else:
                        draw.circle(screen, RED, (int(vals[1]) + 37, int(vals[2]) + 30), 5)
                    
                    vals[4] = str(int(player_x))
                    vals[5] = str(int(player_y))
                    vals[6] = "1"  # if goose huge box colliding with player
                else:
                    if vals[6] == "1":  # if goose colliding box was touching player before
                        # get new target
                        vals[4] = str(int(vals[1]) + random.randrange(-50, 50, 10))
                        vals[5] = str(int(vals[2]) + random.randrange(-50, 50, 10))
                        vals[6] = "0"  # set proximity to not touching player
                
                # geese collision with player - losing hearts
                geese_rect_player = Rect(int(vals[1]) + 20, int(vals[2]) + 20, 70, 75)
                # draw.rect(screen, RED, geese_rect_player, 1)
                if player_rect.colliderect(geese_rect_player) and not immunity:
                    if not mute_button:
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
                    # play different fart sounds depending on what type of poop it is
                    if random_fart == 1:
                        if not mute_button:
                            fart1.play()
                    elif random_fart == 2:
                        if not mute_button:
                            fart2.play()
                    else:
                        if not mute_button:
                            fart3.play()
                    poop_location += str(int(vals[1])) + "," + str(int(vals[2])) + "," + str(random_fart) + ":"
                else:
                    if random.random() < booster_chance:
                        # spawn booster
                        boost_type = random.choice(["Immunity", "Speed"])
                        boost_location += str(int(vals[1])) + "," + str(int(vals[2])) + "," + boost_type + ":"

                # geese animation
                # is current x value less than the target x value, then show move right image, otherwise show move left image
                if int(vals[1]) < int(vals[4]):  # right
                    if current_time % 500 < 250:
                        vals[3] = "3"
                    else:
                        vals[3] = "4"
                else:  # left/stationary
                    if current_time % 500 < 250:
                        vals[3] = "1"
                    else:
                        vals[3] = "2"

                new_location = str(vals[0]) + "," + str(vals[1]) + "," + str(vals[2]) + "," + str(vals[3]) + "," + str(vals[4]) + "," + str(vals[5]) + "," + str(vals[6])
                new_geese_location += new_location + ":"
        
        geese_location = new_geese_location # update geese location


    # check booster collision
    if boost_location:
        for value in boost_location.split(":"):
            if value != "":
                coord = value.split(",")
                booster_rect = Rect(int(coord[0]), int(coord[1]) + 10, 10, 10)
                if player_rect.colliderect(booster_rect): # if player collides with booster
                    if not mute_button:
                        pickup.play()
                    removeBooster(int(coord[0]), int(coord[1])) # remove the booster from the screen
                    if coord[2] == "Immunity":
                        immunity = True
                        immunity_check = 200
                    elif coord[2] == "Speed":
                        speed_boost = True
                        player_speed += 2
                        if player_speed > 10:
                            player_speed = 10
    
    

    # draw player
    screen.blit(player_image, (player_x, player_y))

    # draw hearts
    for num in range(hearts):
        screen.blit(heart, (180 + num * 30, 20))

    # draw score
    score_text = neue_font.render("Score: " + str(score), True, WHITE)
    screen.blit(score_text, (10, 10))

    # draw num poops
    total_poops = 0
    for poop in poop_location.split(":"):
        if poop != "":
            total_poops += 1

    # display how many poops have been collected
    poop_text = neue_font.render("Poops: " + str(total_poops) + "/" + str(max_poops), True, WHITE)
    screen.blit(poop_text, (10, 50))
    if total_poops >= max_poops:
        currentState = GAME_OVER
    
    # Draw level text
    level_text = neue_font.render("Level: " + str(level), True, WHITE)
    screen.blit(level_text, (width - level_text.get_width() - 10, 10))

# draw instructions page
def drawInstructions(screen):
    global mx, my, button, currentState
    
    screen.fill(BLACK)
    
    # Title
    title = neue_font_bold.render("How to Play", True, WHITE)
    screen.blit(title, (width/2 - title.get_width()/2, 50))
    
    # Instructions text
    title = neue_font_bold.render("Controls", True, GOLD)
    screen.blit(title, (width/2 - title.get_width()/2, 150))
    
    text = neue_font.render("Use WASD or Arrow Keys to move", True, WHITE)
    screen.blit(text, (width/2 - text.get_width()/2, 200))
    
    title = neue_font_bold.render("Objective", True, GOLD)
    screen.blit(title, (width/2 - title.get_width()/2, 250))
    
    text = neue_font.render("Avoid the geese and pickup the poop", True, WHITE)
    screen.blit(text, (width/2 - text.get_width()/2, 300))
    
    title = neue_font_bold.render("Power-ups", True, GOLD)
    screen.blit(title, (width/2 - title.get_width()/2, 350))

    # Immunity Power-up
    immunity_image = image.load("assets/images/boosters/immunity.png")
    screen.blit(immunity_image, (width/2 - 310, 405))

    text = neue_font.render("Immunity: Temporary invincibility", True, WHITE)
    screen.blit(text, (width/2 - text.get_width()/2, 400))
    
    # Speed Power-up
    speed_image = image.load("assets/images/boosters/speed.png")
    screen.blit(speed_image, (width/2 - 280, 460))
    
    text = neue_font.render("Speed: Move faster temporarily", True, WHITE)
    screen.blit(text, (width/2 - text.get_width()/2, 450))
    
    title = neue_font_bold.render("Tips", True, GOLD)
    screen.blit(title, (width/2 - title.get_width()/2, 500))
    
    text = neue_font.render("Survive as long as possible", True, WHITE)
    screen.blit(text, (width/2 - text.get_width()/2, 550))
    
    text = neue_font.render("Score increases over time", True, WHITE)
    screen.blit(text, (width/2 - text.get_width()/2, 600))
    
    # Return to menu page button
    return_button = Rect(10, 10, 100, 50)
    draw.rect(screen, GRAY, return_button)
    return_text = small_neue_font.render("Return", True, WHITE)
    screen.blit(return_text, (30, 20))
    
    # Check if return button is clicked
    if return_button.collidepoint(mx, my):
        draw.rect(screen, GOLD, return_button, 2)
    else:
        draw.rect(screen, GRAY, return_button, 2)
    
    # if user clicked the return button
    if button == 1:
        if return_button.collidepoint(mx, my):
            currentState = MENU

# draw leaderboard
def drawLeaderboard(screen):
    global mx, my, button, currentState

    screen.fill(BLACK)

    # text for leaderboard
    leaderboard_text = neue_font_bold.render("Leaderboard", True, WHITE)
    screen.blit(leaderboard_text, (width/2 - leaderboard_text.get_width()/2, 10))

    # text for top 10 scores
    top_scores_text = neue_font.render("Top 10 Scores", True, WHITE)
    screen.blit(top_scores_text, (width/2 - top_scores_text.get_width()/2, 50))

    # draw return button on top left of screen
    return_button = Rect(10, 10, 100, 50)
    draw.rect(screen, GRAY, return_button)
    return_text = small_neue_font.render("Return", True, WHITE)
    screen.blit(return_text, (30, 20))
    
    # check if return button is clicked
    if return_button.collidepoint(mx, my):
        draw.rect(screen, GOLD, return_button, 2)
    else:
        draw.rect(screen, GRAY, return_button, 2)
    
    if button == 1:
        if return_button.collidepoint(mx, my):
            currentState = MENU

    # draw top 10 scores
    # add suff to file - so that if file doesn't exist, will make it
    file = open("leaderboard.txt", "a")
    file.write("")
    file.close()

    file = open("leaderboard.txt", "r")

    # display "name", "score", and "time" text
    name_text = neue_font.render("Name", True, WHITE)
    score_text = neue_font.render("Score", True, WHITE)
    time_text = neue_font.render("Time", True, WHITE)
    screen.blit(name_text, (width / 2 - 300, 150))
    screen.blit(score_text, (width / 2 - 50, 150))
    screen.blit(time_text, (width / 2 + 80, 150))

    # sort the leaderboard by score - inspired by michael
    lines = file.readlines()
    number_list = []
    for line in lines:
        split_lines = line.split(",")
        number_list.append(split_lines[0])
    
    # temporary list to sort the numbers without affecting the original list
    temp_list = []
    for number in number_list:
        temp_list.append(number)
    temp_list.sort(reverse=True)
    sorted_list = []
    for val in temp_list:
        sorted_list.append(lines[number_list.index(val)])
        # remove the used values from the list
        lines.pop(number_list.index(val))
        number_list.remove(val)


    # Display top 10 scores
    for number in range(10):
        split_list = sorted_list[number].split(",")
        score = split_list[0]
        time = split_list[1]
        name = split_list[2].rstrip("\n")
        screen.blit(neue_font.render(str(name), True, WHITE), (width / 2 - 300, 200 + number * 50))
        screen.blit(neue_font.render(str(score), True, WHITE), (width / 2 - 50, 200 + number * 50))
        screen.blit(neue_font.render(str(int(float(time))), True, WHITE), (width / 2 + 80, 200 + number * 50))
    
    if not sorted_list:
        screen.blit(neue_font.render("No scores yet", True, WHITE), (width/2 - 100, height/2 - 50))
    file.close()

# display game over on top of the game
def drawGameOver(screen):
    global score, currentState, restart, level, last_level_increase, goose_speed, maxgeese, poop_chance, entering_name

    # text for game over
    game_over_text = neue_font_bold.render("Game Over", True, WHITE)
    score_text = neue_font.render("Score: " + str(score), True, WHITE) # score
    time_survived_text = neue_font.render("Time Survived: " + str(int(time_survived)) + "s", True, WHITE) # total time survived
    level_text = neue_font.render("Level Reached: " + str(level), True, WHITE) # level reached

    # text background
    draw.rect(screen, GRAY, (width/2 - time_survived_text.get_width()/2 - 10, height/2 - 50, time_survived_text.get_width() + 20, 250))

    # blit text to screen
    screen.blit(game_over_text, (width/2 - game_over_text.get_width()/2, height/2 - game_over_text.get_height()/2))
    screen.blit(score_text, (width/2 - score_text.get_width()/2, height/2 - score_text.get_height()/2 + 50))
    screen.blit(time_survived_text, (width/2 - time_survived_text.get_width()/2, height/2 - time_survived_text.get_height()/2 + 100))
    screen.blit(level_text, (width/2 - level_text.get_width()/2, height/2 - level_text.get_height()/2 + 150))

    display.flip()

    # ask for name if player has top 10 score
    readfile = open("leaderboard.txt", "r")
    filetext = readfile.read()
    filetext = filetext.split("\n")
    
    # Get all valid scores
    valid_scores = []
    for line in filetext:
        if line.strip():  # ignore empty lines
            parts = line.split(",")
            if len(parts) >= 2:
                score_text = parts[0]
                # Check if score is a valid number
                if score_text.isdigit():
                    score_val = int(score_text)
                    valid_scores.append(score_val)
    
    # sorting highest to lowest
    for current_index in range(len(valid_scores)):
        for comparison_index in range(current_index + 1, len(valid_scores)):
            if valid_scores[current_index] < valid_scores[comparison_index]:
                # swap places if current is smaller than next
                temp = valid_scores[current_index]
                valid_scores[current_index] = valid_scores[comparison_index]
                valid_scores[comparison_index] = temp
    
    # Check if current score qualifies for top 10
    qualifies = False
    if len(valid_scores) < 10:
        qualifies = True
    elif len(valid_scores) >= 10 and score > valid_scores[9]:
        qualifies = True
    
    if qualifies:
        # Go to name entry state
        currentState = NAME_ENTRY
        entering_name = True
    else:
        # change states
        restart = True
        # wait 3 seconds
        time.wait(3000)
        currentState = MENU
    
    readfile.close()

# draw name entry screen
def drawNameEntry(screen):
    global currentState, player_name, score, time_survived, restart
    
    screen.fill(BLACK)
    
    # box properties
    box_width = 400
    box_height = 200
    box_x = width//2 - box_width//2
    box_y = height//2 - box_height//2
    
    draw.rect(screen, GRAY, (box_x, box_y, box_width, box_height))
    draw.rect(screen, WHITE, (box_x, box_y, box_width, box_height), 3)
    
    # draw texts
    congrats_text = neue_font.render("New High Score!", True, WHITE)
    screen.blit(congrats_text, (width//2 - congrats_text.get_width()//2, box_y + 20))
    
    instruction_text = small_neue_font.render("Enter your name and press ENTER:", True, WHITE)
    screen.blit(instruction_text, (width//2 - instruction_text.get_width()//2, box_y + 60))
    
    name_box = Rect(box_x + 50, box_y + 100, box_width - 100, 40)
    draw.rect(screen, WHITE, name_box)
    draw.rect(screen, BLACK, name_box, 2)
    
    name_text = neue_font.render(player_name, True, BLACK)
    screen.blit(name_text, (name_box.x + 5, name_box.y + 5))
    
    # cursor
    cursor_x = name_box.x + 5 + name_text.get_width()
    draw.line(screen, BLACK, (cursor_x, name_box.y + 5), (cursor_x, name_box.y + 35), 2)


# Game Loop
while running:
    button = 0

    # get all events
    for e in event.get():
        if e.type == QUIT:
            running = False
        if e.type == MOUSEBUTTONDOWN:
            mx, my = e.pos                             
            button = e.button
        if e.type == MOUSEMOTION:
            mx, my = e.pos
        if e.type == KEYDOWN:
            if currentState == NAME_ENTRY:
                if e.key == K_RETURN:  # Enter key
                    if player_name == "":
                        player_name = "Anonymous"
                    
                    # write score to leaderboard
                    writefile = open("leaderboard.txt", "a")
                    writefile.write(str(score) + "," + str(int(time_survived)) + "," + player_name + "\n")
                    writefile.close()
                    
                    player_name = ""
                    entering_name = False
                    currentState = MENU
                    restart = True
                    
                elif e.key == K_BACKSPACE:  # Backspace key
                    if len(player_name) > 0:
                        player_name = player_name[:-1]  # Remove last character
                        
                else:
                    # limit to 15 characters
                    if len(player_name) < 15:
                        char = e.unicode
                        if char.isalpha() or char.isspace(): # Only letters and spaces
                            player_name += char
            
            # movement keys
            elif currentState == GAME:
                if e.key == K_UP or e.key == K_w: # w or up arrow
                    player_movement[0] = True
                elif e.key == K_DOWN or e.key == K_s: # s or down arrow
                    player_movement[1] = True
                elif e.key == K_LEFT or e.key == K_a: # a or left arrow
                    player_movement[2] = True
                elif e.key == K_RIGHT or e.key == K_d: # d or right arrow
                    player_movement[3] = True
        # key up events
        if e.type == KEYUP:
            # Only handle movement keys when in game
            if currentState == GAME:
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
        # reset game variables
        if restart:
            player_x, player_y = width/2 - 50, height/2 - 50
            hearts = 3
            boosts = []
            geese_location = ""
            poop_location = ""
            boost_location = ""
            score = 0
            time_survived = 0
            restart = False
            level = 1
            last_level_increase = 0
            goose_speed = 2
            maxgeese = 2
            poop_chance = 0.01
            goose_id_counter = 0
            player_speed = 5
            speed_boost = False
            speed_boost_check = 100
            player_movement = [False, False, False, False]
            max_poops = 20

        drawGame(screen)
        time_survived = time.get_ticks() / 1000
        
    # menu states
    elif currentState == INSTRUCTIONS:
        drawInstructions(screen)
    elif currentState == GAME_OVER:
        drawGameOver(screen)
    elif currentState == LEADERBOARD:
        drawLeaderboard(screen)
    elif currentState == NAME_ENTRY:
        drawNameEntry(screen)
    else:
        running = False

    display.flip() # update screen
    clock.tick(FPS)

quit()