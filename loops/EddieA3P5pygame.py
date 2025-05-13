import pygame

pygame.init() # Initialize pygame
import random

# setup the file
file_handle = open("A3P5file.txt", "w")
file_handle.write("Greeting Planet Type\nHello World Caesar")
file_handle.close()

# setup display
SIZE = (1000, 700)
screen = pygame.display.set_mode(SIZE)

# initialize fonts
large_font = pygame.font.SysFont("Arial", 30)
medium_font = pygame.font.SysFont("Arial", 20)
small_font = pygame.font.SysFont("Arial", 18)

# initialize game variables
shift_key = ""

# init pygame variables
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
BLUE = (173, 216, 230)
BROWN = (255, 224, 189)
DARK_BROWN = (139, 69, 19)

screen.fill(BLUE)

# 3 brown backgrounds
pygame.draw.rect(screen, BROWN, (20, 20, 300, 660)) # file
pygame.draw.rect(screen, BROWN, (340, 20, 640, 240)) # input
pygame.draw.rect(screen, BROWN, (340, 280, 640, 400)) # output

# draw 3 white backgrounds
pygame.draw.rect(screen, WHITE, (30, 120, 280, 550)) # file
pygame.draw.rect(screen, BLACK, (30, 120, 280, 550), 1) # border
# input
pygame.draw.rect(screen, WHITE, (360, 340, 600, 330)) # output
pygame.draw.rect(screen, BLACK, (360, 340, 600, 330), 1) # border

# show the texts
file_text = large_font.render("File", 1, DARK_BROWN)
input_text = large_font.render("Input", 1, DARK_BROWN)
output_text = large_font.render("Output", 1, DARK_BROWN)
screen.blit(file_text, (140, 50))
screen.blit(input_text, (610, 50))
screen.blit(output_text, (620, 300))

def display_text(shift_key):
    # display everything in the file
    second_line_file = open("A3P5file.txt", "r")
    append_file = open("A3P5file.txt", "a")

    lines = second_line_file.readlines()

    # encrypt second line
    second_line = lines[1] # get the second line
    
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    alphabet_lower = alphabet.lower()
    newalphabet = alphabet[int(shift_key):] + alphabet[:int(shift_key)] # move the alphabet by the shift key
    newalphabet_lower = alphabet_lower[int(shift_key):] + alphabet_lower[:int(shift_key)] # move the lowercase alphabet by the shift key

    encrypted = ""
    for i in range(len(second_line)):
        index = alphabet.find(second_line[i]) # find the index of the character in the alphabet
        if index != -1:
            encrypted += newalphabet[index] # use the index to find the character in the new alphabet
        elif second_line[i] == " ":
            encrypted += " " # if the character is a space, add a space to the encrypted string
        else:
            # encrypt lowercase characters
            index = alphabet_lower.find(second_line[i])
            if index != -1:
                encrypted += newalphabet_lower[index]
    
    append_file.write("\n" + encrypted) # write the encrypted string to the file
    
    # close the files needed to encrypt the second line
    append_file.close()
    second_line_file.close() 

    # open the file to display all the lists
    open_file = open("A3P5file.txt", "r")
    lines = open_file.readlines()

    y_position = 150  # starting y position
    counter = 0  # line number to add text on top of each list
    words = ["Hints:", "Decoded List:", "Encoded List:"]
    if len(lines) == 3:
        for line in lines:
            line = line.rstrip("\n")  # remove extra \n on the right of the line
            if line:  # only render non-empty lines
                header_text = small_font.render(words[counter], 1, DARK_BROWN)
                file_line_text = small_font.render(str(line.split()), 1, DARK_BROWN)
                screen.blit(header_text, (50, y_position))
                screen.blit(file_line_text, (50, y_position + 25))
                y_position += 100  # move down 50 each line
            counter += 1
    else:
        file_line_text = small_font.render("Add a shift key", 1, DARK_BROWN)
        screen.blit(file_line_text, (50, 550))

    open_file.close()

# shift key
shift_key_text = medium_font.render("Shift Key:", 1, BLACK)
screen.blit(shift_key_text, (380, 180))
pygame.draw.rect(screen, WHITE, (500, 170, 100, 50)) # white input
pygame.draw.rect(screen, BLACK, (500, 170, 100, 50), 1) # border

# input
input_text = medium_font.render("Input:", 1, BLACK)
screen.blit(input_text, (380, 120))
pygame.draw.rect(screen, WHITE, (500, 100, 400, 50)) # white input
pygame.draw.rect(screen, BLACK, (500, 100, 400, 50), 1) # border

shuffled_hints = []
shuffled_message = []
shuffled_encrypted = []
def shuffle_lists():
    global shuffled_hints, shuffled_message, shuffled_encrypted
    # shuffle the lists, using the same index for each list so that the hints match the words
    open_file = open("A3P5file.txt", "r")
    lines = open_file.readlines()
    hints = lines[0].split() # first line
    message = lines[1].split() # second line
    encrypted = lines[2].split() # third line

    temp_hints = hints
    temp_message = message
    temp_encrypted = encrypted

    shuffled_hints = []
    shuffled_message = []
    shuffled_encrypted = []

    # shuffle all the lists with the same index
    for count in range(len(hints)):
        random_index = random.randint(0, len(hints) - 1)
        shuffled_hints.append(temp_hints.pop(random_index))
        shuffled_message.append(temp_message.pop(random_index))
        shuffled_encrypted.append(temp_encrypted.pop(random_index))

def show_output(input):
    print(shuffled_hints, shuffled_message, shuffled_encrypted)

    # clean the output area
    pygame.draw.rect(screen, WHITE, (360, 340, 600, 330)) # white input
    pygame.draw.rect(screen, BLACK, (360, 340, 600, 330), 1) # border

    if input != "none":
        # show encrypted message and hint, compare it with the input to see if it is correct
        if input.lower() == shuffled_message[0].lower():
            # clean the output area
            pygame.draw.rect(screen, WHITE, (360, 340, 600, 330)) # white input
            pygame.draw.rect(screen, BLACK, (360, 340, 600, 330), 1) # border

            # Remove the first element from the lists
            shuffled_hints.pop(0)
            shuffled_message.pop(0)
            shuffled_encrypted.pop(0)
            print(shuffled_hints, shuffled_message, shuffled_encrypted)
            # check if there are no more elements in the list
            if len(shuffled_hints) == 0:
                # if game win
                congrats_text = small_font.render("You win!", 1, DARK_BROWN)
                screen.blit(congrats_text, (400, 380))
                pygame.display.flip()
                pygame.time.delay(2000)
            else:
                # display "correct" message and then give the next encrypted message and hint
                correct_text = small_font.render("Correct! Next word:", 1, DARK_BROWN)
                screen.blit(correct_text, (400, 350))
                # display the next encrypted message and hint
                encrypted_text = small_font.render("Encrypted message: " + shuffled_encrypted[0], 1, DARK_BROWN)
                hint_text = small_font.render("Hint: " + shuffled_hints[0], 1, DARK_BROWN)
                screen.blit(encrypted_text, (400, 380))
                screen.blit(hint_text, (400, 410))
        else:
            # if the input is wrong
            # clean the output area
            pygame.draw.rect(screen, WHITE, (360, 340, 600, 330))
            pygame.draw.rect(screen, BLACK, (360, 340, 600, 330), 1) # border
            # display "incorrect" message
            incorrect_text = small_font.render("Incorrect! Try again:", 1, DARK_BROWN)
            screen.blit(incorrect_text, (400, 350))
            
            # display the encrypted message and hint
            encrypted_text = small_font.render("Encrypted message: " + shuffled_encrypted[0], 1, DARK_BROWN)
            hint_text = small_font.render("Hint: " + shuffled_hints[0], 1, DARK_BROWN)
            screen.blit(encrypted_text, (400, 380))
            screen.blit(hint_text, (400, 410))
            shuffle_lists()
    else:
        shuffle_lists()
        # display the encrypted message and hint
        encrypted_text = small_font.render("Encrypted message: " + shuffled_encrypted[0], 1, DARK_BROWN)
        hint_text = small_font.render("Hint: " + shuffled_hints[0], 1, DARK_BROWN)
        screen.blit(encrypted_text, (400, 350))
        screen.blit(hint_text, (400, 380))


# Ending code
pygame.display.flip()

running = True
shift_clicked = False
input_clicked = False
user_input = ""
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            if 500 <= pygame.mouse.get_pos()[0] <= 600 and 170 <= pygame.mouse.get_pos()[1] <= 220: # clicked on the shift key input
                shift_clicked = True
                input_clicked = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            if 500 <= pygame.mouse.get_pos()[0] <= 900 and 100 <= pygame.mouse.get_pos()[1] <= 150: # clicked on the input area
                input_clicked = True
                shift_clicked = False
        if event.type == pygame.KEYDOWN:
            if shift_clicked:
                if event.key == pygame.K_RETURN: # submit shift key
                    if shift_key:
                        print(shift_key)
                        display_text(shift_key)
                        show_output("none")
                        pygame.display.flip()
                elif event.key == pygame.K_BACKSPACE: # backspace
                    shift_key = shift_key[:-1]
                else:
                    # add numbers to shift key
                    if len(shift_key) < 2:
                        key = event.unicode
                        if key.isdigit():
                            shift_key += key

                # Clear input area
                pygame.draw.rect(screen, WHITE, (500, 170, 100, 50))  # clear input area
                pygame.draw.rect(screen, BLACK, (500, 170, 100, 50), 1)  # redraw border

                # display updated shift_key
                shift_key_text = medium_font.render(shift_key, 1, BLACK)
                screen.blit(shift_key_text, (515, 180))
                pygame.display.flip()

            if input_clicked:
                if event.key == pygame.K_RETURN:
                    if user_input:
                        print(user_input)
                        show_output(user_input)
                        
                        user_input = "" # clear user input

                        pygame.display.flip()
                elif event.key == pygame.K_BACKSPACE:
                    user_input = user_input[:-1]
                else:
                    if len(user_input) < 20:
                        key = event.unicode
                        user_input += key
            
                # Clear input area
                pygame.draw.rect(screen, WHITE, (500, 100, 400, 50))
                pygame.draw.rect(screen, BLACK, (500, 100, 400, 50), 1)
                # display updated user_input
                input_text = medium_font.render(user_input, 1, BLACK)
                screen.blit(input_text, (510, 115))
                pygame.display.flip()
pygame.quit()