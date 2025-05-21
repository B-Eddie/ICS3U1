import random

# 4
file = open("/Users/eddieb/Coding_Projects/ICS3U1/U5/practice/random.txt", "w")

for i in range(1, 1000):
    file.write(str(random.randint(1, 1000)) + "\n")



# 5
fileread = open("/Users/eddieb/Coding_Projects/ICS3U1/U5/practice/random.txt", "r") 
prime = 0
composite = 0
ugly = 0
def checkprime(num):
    if num <= 1:
        return False
    
    for i in range(2, num):
        if num % i == 0:
            return False
    return True

def checkugly(num):
    if num <= 0:
        return False
    
    while num % 2 == 0:
        num //= 2
    while num % 3 == 0:
        num //= 3
    while num % 5 == 0:
        num //= 5
    return num == 1

for i in range(random.randint(1, 1000)):
    if checkprime(i) == True:
        prime += 1
    else:
        composite += 1
        if checkugly(i) == True:
            ugly += 1

print("Prime: %i Composite: %i Ugly: %i" % (prime, composite, ugly))
file.close()