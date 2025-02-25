import math

onedes = input("Please enter a description of the first item bought.: ")
one = int(input("How much was %s: " % onedes))
secdes = input("Please enter a description of the second item bought.: ")
second = int(input("How much was %s: " % secdes))


total = one + second
tax = total * 0.13
entire = total + tax
print("Your purchases come to $%.2f." % total)
print("The HST on your purchases is $%.2f." % tax)
print("The total amount you owe is $%.2f." % entire)
money = float(input("How much money will you give to pay off the total?: "))
print("You receive $%.2f in change." % (money - entire))

