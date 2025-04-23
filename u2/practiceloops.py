import random

guesses_num = 1

rand_num = random.randint(1, 100)

guess = int(input("enter random number"))
while guess != rand_num:
    guesses_num += 1
    if guess > rand_num:
        print("guess is too high")
    elif guess < rand_num:
        print("guess is too low")
    guess = int(input("enter random number"))
print("yey you guessed it in %i guesses" % guesses_num)