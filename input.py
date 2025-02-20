# dinnerCost = int(input("How much u spend on school dinner: "))

# initialMoney = 200

# newmoney = initialMoney - dinnerCost

# print(newmoney)
# for i in range(4):
#     newmoney -= dinnerCost
# print(newmoney, "after 5 days")

# exercise 4
'''1) Write a program that asks the user to input the radius of a circle.  Your program is to then calculate the area and circumference of the circle as follows:

A circle with radius ? cm has a circumference of ? cm and an area of ? cm^2.
2) Write a program that asks for three integers.  Your program calculates the average of the numbers before displaying it appropriately to 2 decimal places.

3) Write a program that asks the user to input their name and then age using separate Prompts. 

Output as follows: My name is ? and I am ? years old.'''

# radius = int(input("Radius: "))
# circumference = 2 * 3.14 * radius
# area = 3.14 * radius ** 2
# print("A circle with radius %i cm has a circumference of %i cm and an area of %i cm^2." %(radius, circumference, area))



# Write a program that asks for three integers.  Your program calculates the average of the numbers before displaying it appropriately to 2 decimal places.
# one = int(input("Enter first number: "))
# two = int(input("Enter second number: "))
# three = int(input("Enter third number: "))
# average = (one + two + three) / 3
# print("The average of the numbers is %.2f" %average)

# Write a program that asks the user to input their name and then age using separate Prompts. 
#Output as follows: My name is ? and I am ? years old.
# name = input("Enter your name: ")
# age = int(input("Enter your age: "))
# print("My name is %s and I am %i years old." %(name, age))


# Problem 2
# Given an amount of change less than 99 cents,
# calculate how many quarters, dimes, nickels and pennies (pennies still exist in this question!) it would take to total the amount. Your program will have in-line documentation (a header and in-line comments). Give your program an appropriate name.

# change = int(input("Enter the amount of change: "))
# quarters = change // 25
# change = change % 25
# dimes = change // 10
# change = change % 10
# nickels = change // 5
# change = change % 5
# pennies = change

# print("-----------------------------------")
# print("Quarters: %i\nDimes: %i\nNickels: %i\nPennies: %i" %(quarters, dimes, nickels, pennies))
# print("-----------------------------------")


# Quadratic Formula
# yes = input()
# a = int(input("Enter A: "))
# b = int(input("Enter B: "))
# c = int(input("Enter C: "))
# root1 = (-b + (b ** 2 - 4 * a * c) ** 0.5) / (2 * a)
# root2 = (-b - (b ** 2 - 4 * a * c) ** 0.5) / (2 * a)
# print("The roots are: %i, %i" %(root1, root2))