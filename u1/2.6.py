# firstName = input("What is your first name?: ")
# lastName = input("What si your last name?: ")

# print(firstName[0].upper() + ". " + lastName.capitalize())

# fullName = input("What is your full name?: ")
# print(fullName[fullName.find(" "):].upper() + ", " + fullName[:fullName.find(" ") + 1])

# num = input("Enter a number: ")
# print(("X"*int(num) + "\n")*int(num))

# combination = input("What is your locker combination: ")
# firstSpace = combination.find("-")
# second = combination[firstSpace+1:]
# print(int(combination[:combination.find("-")]) + int(combination[firstSpace+1:combination[firstSpace+1].find("-")-1]) + int(second[second.find("-")+1:]))