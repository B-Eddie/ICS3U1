# Name: Eddie Bian
# Date: April 2, 2025
# Course Code: ICS3U1
# Description: collision chcker circle

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

# function to check if user input is correct
def check_for_errors(string, character, name, error_messages, first_index, last_index):
    # this function checks if the user input is valid and adds errors if there are any

    string_split = string[first_index:last_index]
    if string.count(character) > 1:
        error_messages += "\n - too many %ss" % name
    elif string.count(character) == 0:
        error_messages += "\n - missing %s" % name
    elif string_split.count(character) != string.count(character):
        error_messages += "\n - %s at wrong place" % name
    
    return error_messages
   
# get values from user and print where the fixed circle is
print("The fixed circle is at (%s, %s) and the radius is %s" % (fixed_circle_x, fixed_circle_y, fixed_circle_radius) )
user_input = input("Enter the x, y, and radius of the circle in the format: (x,y) radius: ")

# # Clean the user input
# replace everything except the numbers with spaces
cleaned_input = user_input.replace('(', " ").replace(")", " ").replace(",", " ")

if cleaned_input.replace(" ", "").replace("-", "").isdigit():
    # removes all spaces from the start and end of string (trailing and leading spaces)
    cleaned_input = cleaned_input[cleaned_input.find(cleaned_input.replace(" ", "")[0]):len(cleaned_input) - cleaned_input[::-1].find(cleaned_input[-1])]

    # call the split function on the user string & remove the first space that the function creates
    # parsed_values = split(cleaned_input, " ", "")[1:]
    parsed_values = split(cleaned_input, " ", "")[1:]

    # check if user input is valid & do the calculations
    if parsed_values.count(" ") == 2:
        # separate the user input into 3 variables
        user_x = parsed_values[0:parsed_values.find(" ")]
        user_y = parsed_values[parsed_values.find(" ") + 1:parsed_values.find(" ", parsed_values.find(" ") + 1)]
        radius = parsed_values[parsed_values.find(" ", parsed_values.find(" ") + 1) + 1:len(parsed_values)]

        # get the index numbers of each input
        user_x_index = user_input.find(user_x)
        user_y_index = user_input[user_x_index + len(user_x):].find(user_y) + user_x_index + len(user_x)
        radius_index = user_input[user_y_index + len(user_y):].find(radius) + user_y_index + len(user_y)

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
                # Check the user input if it matches the format
                # call the checking error function for all the characters
                error_messages = check_for_errors(user_input, "(", "left bracket", "These are the errors in your formatting:", 0, user_x_index)
                error_messages = check_for_errors(user_input, ")", "right bracket", error_messages, user_y_index, radius_index)
                error_messages = check_for_errors(user_input, ",", "comma", error_messages, user_x_index, user_y_index)
                error_messages = check_for_errors(user_input, " ", "space", error_messages, user_y_index, radius_index)

                # print the errors if there are any
                if error_messages.count("\n") > 0:
                    print("-------------------")
                    print(error_messages)
                    print("-------------------")
                    print("But I can still use the inputs :D\n")

                # when the input is fine
                print("Your circle is at (%i, %i) and the radius is %i" % (int(user_x), int(user_y), int(radius)))
                
                # variable for the output of the program
                collision_status = "" 
                
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
                    if fixed_circle_radius == radius and user_x == fixed_circle_x and user_y == fixed_circle_y and radius != 0:
                        collision_status = "Circles are the same"
                    elif distance < abs(fixed_circle_radius - radius) and user_x + radius < fixed_circle_x + fixed_circle_radius and user_y + radius < fixed_circle_y + fixed_circle_radius:
                        collision_status = "Circle is inside the other circle, but not touching"
                    elif distance < abs(fixed_circle_radius - radius) and user_x + radius > fixed_circle_x + fixed_circle_radius and user_y + radius > fixed_circle_y + fixed_circle_radius:
                        collision_status = "Circle is outside the other circle, but not touching"
                    elif distance + radius == fixed_circle_radius:
                        collision_status = "Circle is touching the inside of the fixed circle at one point"

                # check where the point is relative to the fixed circle
                elif (user_x - fixed_circle_x)**2 + (user_y - fixed_circle_y)**2 == fixed_circle_radius**2:
                    print("Center point is on the circle")
                else: # if the point isn't on the circle or inside the circle, it is outside the circle
                    print("Center point is outside the circle")

                # check if the circles are touching
                if distance == fixed_circle_radius + radius: # circles touching only once
                    collision_status = "Circles are touching at one point"
                elif distance < fixed_circle_radius + radius and distance > abs(fixed_circle_radius - radius): # circles touching at two points
                    collision_status = "Circles are overlapping"
                else: # if the cicles aren't touching anywhere, the circles aren't touching at all
                    if collision_status == "":
                        collision_status = "Circles are not touching"
                
                # print how circles are touching
                print(collision_status)
        elif radius.count("-") > 0: # if the radius is negative
            print("radius can't be negative")
    elif parsed_values.count(" ") > 2:
        print("too many points")
    else:
        print("not enough points")
else:
    print("Containing non-numeric characters")

