import math
# students = input("Please enter the number of students: ")
# agesum = input("What is the sum of their ages?: ")

# print("The average of their ages is %.2f" % (int(agesum) / int(students)))

# circumference = int(input("What is the circumference of the circle?: "))
# radius = circumference / (2 * math.pi)
# print("A circle with circumference %i has a radius of %.2f." % (circumference, radius))

# time = input("What is the time in HH:MM format?: ")
# hours = time[:time.find(":")]
# minutes = time[time.find(":")+1:]
# totalMinutes = int(hours) * 60 + int(minutes)
# print("%s represents %i minutes." % (time, totalMinutes))

number = input("What is your four digits number?: ")
sum = int(number[0]) + int(number[1]) + int(number[2]) + int(number[3])
print("The sum of the digits is %i." % (sum))

average = sum / 4
print("The average of the digits is %.2f." % (average))
print("The reverse of the number is %s." % (number[3] + number[2] + number[1] + number[0]))
