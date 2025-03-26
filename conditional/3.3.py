# Write a program that asks the user to input any two numbers.  Output which is 
# the largest of those two numbers.

# 2)	Write a program that asks the user to input any two numbers.  Output the 
# numbers in order from greatest to smallest.

# 3)	Write a program that asks the user to input any three numbers.  Output the 
# largest of the three numbers.

# 4)	Write a program that asks the user to input any three numbers.  Output the 
# numbers in order from greatest to smallest.

num1 = int(input("Enter a number: "))
num2 = int(input("Enter a number: "))
num3 = int(input("Enter a number: "))
if num1 > num2:
    if num2 > num3:
        print(num1, num3, num2)
    else:
        print(num1, num2, num3)
else:
    if num1 > num3:
        print(num2, num1, num3)
    else:
        print(num3, num1, num2)
