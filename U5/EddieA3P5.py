# Name: Eddie Bian
# Date: May 7, 2025
# Course Code: ICS3U1
# Description: Mystery Message Decoder

import random

# initialize inputs
message = input("Enter a 5 word message: ")
hints = input("Enter a 5 word hint list: ")
shift = input("Enter shift value: ")

if len(message.split()) != 5 or len(hints.split()) != 5: # check if the message and hint list are 5 words
    print("\nError, message and hint list must be 5 words")
elif not message.replace(" ", "").isalpha() or not hints.replace(" ", "").isalpha(): # check if the message and hint list are alphabetic
    print("\nError, message and hint list must be alphabetic")
elif not shift.isdigit(): # check if the shift value is a number
    print("\nError, shift value must be a number")
elif not 0 <= int(shift) <= 25: # check if the shift value is between 0 and 25
    print("\nError, shift value must be between 0 and 25")
else:
    shift = int(shift) # cast shift to an integer

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
            # if the wordlist is empty, move all the words in the other list to the wordlist and hintlist
            for eachword in newwordlist:
                wordlist.append(eachword)
            for eachhint in newhintlist:
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
    print("Original:", newwordlist)
    print("Encrypted:", encrypted)
    print("Hint list:", newhintlist)
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
            print("Original:", newwordlist)
            print("Encrypted:", encrypted)
            print("hint list:", newhintlist)
            # encrypted = encrypted.split()
            num = 0
