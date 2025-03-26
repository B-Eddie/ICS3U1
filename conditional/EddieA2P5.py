# Name: Eddie Bian
# Date: March 6, 2025
# Course Code: ICS3U1
# Description: collision chcker

import math

# define the fixed circle
circle_x = 10
circle_y = 10
circle_radius = 20

point_coord = input("Enter the x, y, and radius of the circle ((x,y) radius): ")

# get the x, y, and radius of the user inputted circle
cleaned_point = point_coord.replace("(", "")
cleaned_point = cleaned_point.replace(")", "")
cleaned_point = cleaned_point.replace(",", " ")
cleaned_point = cleaned_point.replace("  ", " ")

if cleaned_point.count(" ") == 2:
    # extract the x, y, radius from the user input
    user_x = cleaned_point[:cleaned_point.find(" ")].replace(" ", "")
    user_y = cleaned_point[cleaned_point.find(" ")+1:][:cleaned_point[cleaned_point.find(" ")+1:].find(" ")].replace(" ", "")
    radius = cleaned_point[cleaned_point.find(" ")+1:][cleaned_point[cleaned_point.find(" ")+1:].find(" "):].replace(" ", "")
    
    if user_x.isdigit() == False or user_y.isdigit() == False or radius.isdigit() == False:
        print("Invalid input - not a number")
    
    else:
        print(user_x)
        print(user_y)
        print(radius)

        circle_touching = ""

        # Calculate where the user point is relative to the circle
        # check x values if point is inside circle
        if int(user_x) > circle_x - circle_radius and int(user_x) < circle_x + circle_radius:
            # check y values if point is inside circle
            if int(user_y) > circle_y - circle_radius and int(user_y) < circle_y + circle_radius:
                print("Point is inside the circle")
                # check if circle is inside other circle but the circles aren't touching
                if int(user_x) + int(radius) < circle_x + circle_radius and int(user_y) + int(radius) < circle_y + circle_radius :
                    circle_touching = "Circle is inside the other circle, but not touching"
        elif (int(user_x) - circle_x)**2 + (int(user_y) - circle_y)**2 == circle_radius**2:
            print("Point is on the circle")
        else: # if the point isn't on the circle or inside the circle, meaning it is outside the circle
            print("Point is outside the circle")

        # distance between two center points
        distance = math.sqrt((int(user_x) - circle_x)**2 + (int(user_y) - circle_y)**2)
        # check if the circles are touching
        if distance == circle_radius + int(radius):
            circle_touching = "Circles are touching at one point"
        elif distance < circle_radius + int(radius):
            circle_touching = "Circles are overlapping"

        if len(circle_touching) == 0: # can i do this
            circle_touching = "Circles are not touching"
        
        print(circle_touching)
else:
    print("Invalid input - not enough points")