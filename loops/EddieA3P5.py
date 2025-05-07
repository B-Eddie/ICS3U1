# # Name: Eddie Bian
# # Date: May 20, 2025
# # Course Code: ICS3U1
# # Description: Mystery Message Decoder

import pygame
import random

# pygame.init() # Initialize pygame

# # Setup display
# SIZE = (1000, 700)
# screen = pygame.display.set_mode(SIZE)

# BLACK = (0, 0, 0)


message = input("Enter a message: ")
hints = input("Enter hints: ")
shift = int(input("Enter shift value: "))

alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
newalphabet = alphabet[shift:] + alphabet[:shift]
encrypted = ""
for i in message:
    i = i.upper()
    print(i, alphabet.find(i))
    if i == " ":
        encrypted += " "
    else:
        encrypted += newalphabet[alphabet.find(i.upper())]
print("Encrypted message:", encrypted)

wordlist = message.split()
otherwordlist = hints.split()
newwordlist = []
newotherwordlist = []
def shufflelists():
    for i in range(len(alphabet)):
        if len(wordlist) == 0:
            break
        else:
            random_index = random.randint(0, len(wordlist) - 1)
            print(wordlist)
            j = wordlist.pop(random_index)
            k = otherwordlist.pop(random_index)
            newwordlist.append(j)
            newotherwordlist.append(k)
shufflelists()

encrypted = encrypted.split()

game = True
num = 0
while game:
    if num >= len(newwordlist):
        print("Congratulations! You've completed the game.")
        break
    print("encrypted word: " + encrypted[num])
    print("hint: " + newotherwordlist[num])
    guess = input("Guess the word: ")
    if guess == newwordlist[num]:
        print("Correct!\n")
        num += 1
    else:
        print("Incorrect! Reshuffling... Try again.")
        shufflelists()
        num = 0

    
print("New word list:", newwordlist)
print("New other word list:", newotherwordlist)