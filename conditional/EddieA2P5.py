# Name: Eddie Bian
# Date: March 26, 2025
# Course Code: ICS3U1
# Description: collision chcker

import math

# define the fixed circle
fixed_circle_x = 0
fixed_circle_y = 0
fixed_circle_radius = 10


# function to split string, using recursion
def split(string, split_by, split_string):
    # This function splits a string based on a given character and returns the split string    


    # check if the first index is a space
    if string.find(split_by) == 0:
        # if the character is a space
        return split(string[1:], split_by, split_string)
    
    # the last numbers of the string that don't have any spaces
    if string.count(split_by) == 0:
        if string != "":
            split_string += " "
            split_string += string
        return split_string
        
    else:
        # add the string up to the split character to the split string
        split_string += " "
        split_string += string[0:string.find(split_by)]
        return split(string[string.find(split_by) + 1:], split_by, split_string)

# get values from user and print where the fixed circle is
print("The fixed circle is at (%s, %s) and the radius is %s" % (fixed_circle_x, fixed_circle_y, fixed_circle_radius) )
point_coord = input("Enter the x, y, and radius of the circle in the format: (x,y) radius: ")

stuff_missing = "This is the stuff you're not following:\n"

# check the user input if it matches the format
if split(point_coord, "(", "").count(" ") > 1:
    stuff_missing += "too many left brackets"
elif split(point_coord, "(", "").count(" ") == 0:
    stuff_missing += "missing left bracket\n"


# Clean the user input - this is the this receives all the 
# replace everything except the numbers with spaces
removed_all_spaces = point_coord.replace('(', " ").replace(")", " ").replace(",", " ").replace(" ", " ")

# removes all spaces from the start and end of string (trailing and leading spaces)
removed_all_spaces = removed_all_spaces[removed_all_spaces.find(removed_all_spaces.replace(" ", "")[0]):len(removed_all_spaces) - removed_all_spaces[::-1].find(removed_all_spaces[-1])]

# call the split function on the user string and remove the first space created from the function
cleaned_points = split(removed_all_spaces, " ", "")[1:] 
# check if user input is valid & do the calculations
if cleaned_points.count(" ") == 2:
    # separate the user input into 3 variables
    user_x = cleaned_points[0:cleaned_points.find(" ")]
    user_y = cleaned_points[cleaned_points.find(" ") + 1:cleaned_points.find(" ", cleaned_points.find(" ") + 1)]
    radius = cleaned_points[cleaned_points.find(" ", cleaned_points.find(" ") + 1) + 1:len(cleaned_points)]
    
    # check if all the numbers are digits
    if user_x.replace("-", "").isdigit() == True and user_y.replace("-", "").isdigit() == True and radius.isdigit() == True:
        # check if the radius is 0
        if radius == "0":
            print("Radius is 0 - circle aint a circle")

        # check if the dashes are in the right place
        if user_x.count("-") > 1 or user_y.count("-") > 1: # if the x or y value has more than one dash
            print("too many dashes in x or y values")
        elif user_x.count("-") == 1 and user_x[0] != "-" or user_y.count("-") == 1 and user_y[0] != "-": # if the x or y value has a dash in the wrong place
            print("dashes in the wrong place")
        else:
            print("Your circle is at (%s, %s) and the radius is %s" % (user_x, user_y, radius))
            circle_touching = "" # variable for the output of the program
            # cast the variables into integers
            user_y = int(user_y)
            radius = int(radius)
            user_x = int(user_x)

            # Calculate distance between two center points of user and fixed circle
            distance = math.sqrt((user_x - fixed_circle_x)**2 + (int(user_y) - fixed_circle_y)**2)

            # Calculate where the user point is relative to the circle
            # check x and y values if point is inside circle
            if user_x > fixed_circle_x - fixed_circle_radius and user_x < fixed_circle_x + fixed_circle_radius and user_y > fixed_circle_y - fixed_circle_radius and user_y < fixed_circle_y + fixed_circle_radius:
                print("Center point is inside the circle")
                # check how the circle is inside the fixed circle 
                if fixed_circle_radius == radius and user_x == fixed_circle_x and user_y == fixed_circle_y:
                    circle_touching = "Circles are the same"
                elif distance < abs(fixed_circle_radius - radius) and user_x + radius < fixed_circle_x + fixed_circle_radius and user_y + radius < fixed_circle_y + fixed_circle_radius:
                    circle_touching = "Circle is inside the other circle, but not touching"
                elif distance < abs(fixed_circle_radius - radius) and user_x + radius > fixed_circle_x + fixed_circle_radius and user_y + radius > fixed_circle_y + fixed_circle_radius:
                    circle_touching = "Circle is outside the other circle, but not touching"
                elif distance + radius == fixed_circle_radius:
                    circle_touching = "Circle is touching the inside of the fixed circle at one point"

            # check where the point
            elif (user_x - fixed_circle_x)**2 + (user_y - fixed_circle_y)**2 == fixed_circle_radius**2:
                print("Center point is on the circle")
            else: # if the point isn't on the circle or inside the circle, it is outside the circle
                print("Center point is outside the circle")

            # check if the circles are touching
            if distance == fixed_circle_radius + radius: # circles touching only once
                circle_touching = "Circles are touching at one point"
            elif distance < fixed_circle_radius + radius and distance > abs(fixed_circle_radius - radius): # circles touching at two points
                circle_touching = "Circles are overlapping"
            else: # if the cicles aren't touching anywhere, the circles aren't touching at all
                if circle_touching == "":
                    circle_touching = "Circles are not touching"
            
            # print how to circles are touching
            print(circle_touching)
    else:
        if radius.isdigit() != True and radius.replace("-", "").isdigit() == True: # if the radius has a dash in it
            print("radius can't be negative")
        else:
            print("containing non-numeric characters")
elif cleaned_points.count(" ") > 2:
    print("too many points")
else:
    print("not enough points")