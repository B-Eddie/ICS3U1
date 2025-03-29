# Name: Eddie Bian
# Date: March 26, 2025
# Course Code: ICS3U1
# Description: collision chcker

import math

# define the fixed circle
circle_x = 0
circle_y = 0
circle_radius = 10

point_coord = input("Enter the x, y, and radius of the circle ((x,y) radius): ")

# get the x, y, and radius of the user inputted circle
removed_all_spaces = point_coord.replace('(', " ").replace(")", " ").replace(",", " ").replace(" ", " ")

def split(string, split_by, split_string):
    # implement a recursive approach to split the string
    if string.find(split_by) == 0:
        # if the character is a space
        return split(string[1:], split_by, split_string)
    
    if string.count(split_by) == 0:
        # last part of the string
        if string != "":
            split_string += " "
            split_string += string
        return split_string
    else:
        # add the string up to the split character to the split string
        split_string += " "
        split_string += string[0:string.find(split_by)]
        return split(string[string.find(split_by) + 1:], split_by, split_string)

print(removed_all_spaces)
# removes all spaces from the start end end of string
removed_all_spaces = removed_all_spaces[removed_all_spaces.find(removed_all_spaces.replace(" ", "")[0]):len(removed_all_spaces) - removed_all_spaces[::-1].find(removed_all_spaces[-1])]
print("removed", removed_all_spaces + "a")
cleaned_points = split(removed_all_spaces, " ", "")[1:] # remove the first space created from the function
print(cleaned_points + "a")
print("num poitns" + str(cleaned_points.count(" ")))
# check if user input is valid & do the calculations
if cleaned_points.count(" ") == 2:
    user_x = cleaned_points[0:cleaned_points.find(" ")]
    user_y = cleaned_points[cleaned_points.find(" ") + 1:cleaned_points.find(" ", cleaned_points.find(" ") + 1)]
    radius = cleaned_points[cleaned_points.find(" ", cleaned_points.find(" ") + 1) + 1:len(cleaned_points)]
    print(user_x)
    print(user_y)
    print(radius)
    if user_x.replace("-", "").isdigit() == True and user_y.replace("-", "").isdigit() == True and radius.isdigit() == True:
        if radius == "0":
            print("Radius is 0 - circle aint a circle") # is it suppose to allow this

        if user_x.isalpha() == True or user_y.isalpha() == True or radius.isalpha() == True:
            print("Invalid input - not a number")
        else:
            circle_touching = ""
            user_y = int(user_y)
            radius = int(radius)
            user_x = int(user_x)

            # Calculate distance between two center points of user and fixed circle
            distance = math.sqrt((user_x - circle_x)**2 + (int(user_y) - circle_y)**2)
            # Calculate where the user point is relative to the circle
            # check x values if point is inside circle
            if user_x > circle_x - circle_radius and user_x < circle_x + circle_radius:
                # check y values if point is inside circle
                if user_y > circle_y - circle_radius and user_y < circle_y + circle_radius:
                    print("Point is inside the circle")
                    # check if circle is inside other circle but the circles aren't touching
                    # if user_x + radius < circle_x + circle_radius and user_y + radius < circle_y + circle_radius:
                    if circle_radius == radius and user_x == circle_x and user_y == circle_y:
                        circle_touching = "Circles are the same"
                    elif distance < abs(circle_radius - radius) and user_x + radius < circle_x + circle_radius and user_y + radius < circle_y + circle_radius:
                        circle_touching = "Circle is inside the other circle, but not touching"
                    elif distance < abs(circle_radius - radius) and user_x + radius > circle_x + circle_radius and user_y + radius > circle_y + circle_radius:
                        circle_touching = "Circle is outside the other circle, but not touching"
                    elif distance + radius == circle_radius:
                        circle_touching = "Circle is touching the inside of other circle once"
            elif (user_x - circle_x)**2 + (user_y - circle_y)**2 == circle_radius**2:
                print("Point is on the circle")
            else: # if the point isn't on the circle or inside the circle, meaning it is outside the circle
                print("Point is outside the circle")

            # distance between two center points
            # check if the circles are touching
            if distance == circle_radius + radius and radius != "0": # touching only once
                circle_touching = "Circles are touching at one point"
            elif distance < circle_radius + radius and distance > abs(circle_radius - radius): # touching twice
                circle_touching = "Circles are overlapping"
            else:
                if circle_touching == "":
                    circle_touching = "Circles are not touching"
            print(circle_touching)
    else:
        if radius.isdigit() != True and radius.replace("-", "").isdigit() == True:
            print("Invalid input - radius can't be negative")
        else:
            print("Invalid input - containing non-numeric characters")
elif cleaned_points.count(" ") > 2:
    print("Invalid input - too many points")
else:
    print("Invalid input - not enough points")