import random

string = ""
for i in range(random.randint(5, 10)):
    string += str(random.randint(0, 9))

newstring = string[::-1]

finalstring = ""
for i in range(0, len(string)):
    newone = int(string[i]) + int(newstring[i])
    if newone % 2 == 0:
        finalstring += "0" + str(newone) + "0"
    else:
        finalstring += str(newone * (i + 1))

print("." + string)
print("." + newstring)
print("." + finalstring)