# Name: Eddie Bian
# Date: March 26, 2025
# Course Code: ICS3U1
# Description: collision chcker

import math

# define the fixed circle
circle_x = -2
circle_y = -2
circle_radius = 2

point_coord = input("Enter the x, y, and radius of the circle ((x,y) radius): ")

# get the x, y, and radius of the user inputted circle
removed_all_spaces = point_coord.replace('(', "").replace(")", "").replace(",", "").replace(" ", "")
if len(removed_all_spaces) < 3:
    print("Invalid input - not enough points")
else:
    # get everything in between the first and last digit
    points = (point_coord[point_coord.find(removed_all_spaces[0]):len(point_coord) - point_coord[::-1].find(removed_all_spaces[-1])])
    new_points = ""

    all_space = points.replace(",", " ").replace("(", " ").replace(")", " ")
    # extract the x, y, radius from the user input
    # first num
    user_x = all_space[:all_space.find(" ")] # from the start to the first space
    new_points = all_space[all_space.find(all_space[all_space.find(" ") + 1:].replace(" ", "")[0]):] # from the first space to the end (everything excluding first num)
    if new_points.count(" ") < 2:
        print("Invalid input - not enough points")
    else:
        # second num
        user_y = new_points[:new_points.find(" ")]
        new_points = new_points[new_points.find(new_points[new_points.find(" ") + 1:].replace(" ", "")[0]):]
        print(new_points.count(" "))
        # third num
        radius = new_points.replace(" ", "")
        cleaned_point = user_x + user_y + radius

        # check if user input is valid & do the calculations
        if cleaned_point.count(" ") == 0:
            print(user_x)
            print(user_y)
            print(radius)
            if user_x.isalpha() == True or user_y.isalpha() == True or radius.isalpha() == True:
                print("Invalid input - not a number")
            
            else:
                circle_touching = ""
                user_y = int(user_y)
                radius = int(radius)
                user_x = int(user_x)

                # Calculate where the user point is relative to the circle
                # check x values if point is inside circle
                if user_x > circle_x - circle_radius and user_x < circle_x + circle_radius:
                    # check y values if point is inside circle
                    if user_y > circle_y - circle_radius and user_y < circle_y + circle_radius:
                        print("Point is inside the circle")
                        # check if circle is inside other circle but the circles aren't touching
                        if user_x + radius < circle_x + circle_radius and user_y + radius < circle_y + circle_radius :
                            circle_touching = "Circle is inside the other circle, but not touching"
                elif (user_x - circle_x)**2 + (user_y - circle_y)**2 == circle_radius**2:
                    print("Point is on the circle")
                else: # if the point isn't on the circle or inside the circle, meaning it is outside the circle
                    print("Point is outside the circle")

                # distance between two center points
                distance = math.sqrt((user_x - circle_x)**2 + (int(user_y) - circle_y)**2)
                # check if the circles are touching
                if distance == circle_radius + radius:
                    circle_touching = "Circles are touching at one point"
                elif distance < circle_radius + radius:
                    circle_touching = "Circles are overlapping"

                if len(circle_touching) == 0: # can i do this
                    circle_touching = "Circles are not touching"
                
                print(circle_touching)
        elif cleaned_point.count(" ") > 0:
            print("Invalid input - too many points")
        elif cleaned_point.isdigit() == False:
            print("Invalid input - not a number")
        else:
            print("Invalid input - not enough points")