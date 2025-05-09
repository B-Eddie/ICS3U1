# Name: Eddie Bian
# Date: May 20, 2025
# Course Code: ICS3U1
# Description: Mystery Message Decoder

import pygame
import random

# pygame.init() # Initialize pygame

# # Setup display
# SIZE = (1000, 700)
# screen = pygame.display.set_mode(SIZE)
# text = pygame.font.SysFont("Arial", 30) # initialize fonts

# # init pygame variables
# BLACK = (0, 0, 0)
# WHITE = (255, 255, 255)
# BLUE = (173, 216, 230)
# BROWN = (255, 224, 189)
# DARK_BROWN = (139, 69, 19)

# screen.fill(BLUE)

# pygame.draw.rect(screen, BROWN, (20, 20, 300, 660))
# pygame.draw.rect(screen, BROWN, (340, 20, 640, 240))
# pygame.draw.rect(screen, BROWN, (340, 280, 640, 400))

# # show the texts
# fileText = text.render("File", 1, DARK_BROWN)
# inputText = text.render("Input", 1, DARK_BROWN)
# outputText = text.render("Output", 1, DARK_BROWN)
# screen.blit(fileText, (140,50,100,50))	
# screen.blit(inputText, (610,50,100,50))	
# screen.blit(outputText, (620,300,100,50))	

# # Ending code
# pygame.display.flip()
# running = True
# while running:
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             running = False

# pygame.quit()

# exit() # ! remove after
# initialize inputs
message = input("Enter a message: ")
hints = input("Enter hints: ")
shift = int(input("Enter shift value: "))

# two alphabets, one for uppercase and one for lowercase
alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
alphabet_lower = alphabet.lower()

# shift the alphabets by the shift values
newalphabet = alphabet[shift:] + alphabet[:shift]
newalphabet_lower = alphabet_lower[shift:] + alphabet_lower[:shift]

# encrypt the message using the shifted alphabets
encrypted = ""
for i in message:
    # if the character is a space
    if i == " ":
        encrypted += " "
    else:
        # add the encrypted character of each letter
        # if the character is uppercase
        letter = alphabet.find(i)
        if letter == -1:
            letter = alphabet_lower.find(i)
            encrypted += newalphabet_lower[letter]
        else:
            # if the character is lowercase
            encrypted += newalphabet[letter]

# print("Encrypted message:", encrypted)

# split the message and hints into lists
wordlist = message.split()
hintlist = hints.split()
encrypted = encrypted.split()
newwordlist = []
newhintlist = []

# shuffle the lists, using the same index for each list so that the hints match the words
def shufflelists():
    global wordlist, hintlist, encrypted, newwordlist, newhintlist
    if len(wordlist) == 0:
        for eachword in newwordlist:
            # removeword = newwordlist.pop(newwordlist.index(eachword))
            wordlist.append(eachword)
        for eachhint in newhintlist:
            # removehint = newhintlist.pop(newhintlist.index(eachhint))
            hintlist.append(eachhint)
        newwordlist = []
        newhintlist = []

    for count in range(len(wordlist)):
        # if the wordlist is empty, break the loop
        if len(wordlist) == 0:
            break
        else:

            random_index = random.randint(0, len(wordlist) - 1)

            tempword = wordlist.pop(random_index)
            newwordlist.append(tempword)

            temphint = hintlist.pop(random_index)
            newhintlist.append(temphint)

            tempencrypted = encrypted.pop(random_index)
            encrypted.append(tempencrypted)

shufflelists() # call the shuffle function

# start the game loop
game = True
num = 0
while game:
    # print("New word list:", encrypted)
    # print("New other word list:", newhintlist)
    # encrypted = encrypted.split()
    
    # if there are no more remaining words, break the loop
    if num >= len(newwordlist):
        print("Congratulations! You've completed the game.")
        break

    # give the encrypted word and hint
    print("encrypted word: " + encrypted[num])
    print("hint: " + newhintlist[num])
    # retrieve the guess from the user input
    guess = input("Guess the word: ")
    if guess.lower() == newwordlist[num].lower():
        print("Correct!\n")
        num += 1
    else:
        # if the guess is incorrect, reshuffle the lists
        print("Incorrect! Reshuffling... Try again.\n")
        shufflelists()
        # ! doesn't wor
        # encrypted = encrypted.split()
        num = 0
