# This is entirely to convert coordinates between two systems.
# Cartesian Coordinates has x,y coordinate pair
# print('x,y - This is cartesion coordinate')
# print('r,Θ - This is the polar coordinate')
import time
import math

while True:
    time.sleep(1)
    print("These are the available options: [Cartesian, Polar]. 1 represents cartesian, while 2 represents Polar")
    try:
        time.sleep(1)
        coord_type = int(input("Enter the Coordinate type from the list above : "))
        if coord_type == 1 or coord_type == 2:
            print("Input received successfully!")
            break;
        else:
            print("Enter a valid option. Choose between 1 for Cartesian and 2 for Polar")
            
    except ValueError:
        print("Enter a valid value")
        continue

time.sleep(2)
# conditional if statements to filter value
if coord_type == 1:
    print("You are about to convert from Cartesian to Polar. Enter x and y coordinate pair")
    while True:
        try:
            
            time.sleep(1)
            x = float(input("Enter the x value : "))
            
            if x == 0:
                print("Enter a value more than 0")
            else:
                print("x input received successfully! Now enter y")
                break;
        except ValueError:
            print("Enter a numeric value!")
            continue
    while True:
        try:
            
            time.sleep(1)
            
            y = float(input("Enter the y value : "))
            if y == 0:
                print("Enter a value more than 0")
            else:
                print("y input received successfully!")
                break;
        except ValueError:
            print("Enter a numeric value!")
            continue
    
    time.sleep(1)
    # Let's now convert to Polar
    def cartesianToPolar(x, y):
        hypp = x*x + y*y
        hyp = math.sqrt(hypp)
        tanΘ = y/x
        tanΘ = math.degrees(math.atan(tanΘ))
        #print(hyp, round(tanΘ, 2))
        tanΘ = round(tanΘ, 2)
        tanΘ = str(tanΘ)+'°'
        polar = (hyp, tanΘ)
        
        return polar
        
    cartesianToPolar(x, y)
    print("Conversion has been successful!")
    time.sleep(1)
    print("The results obtained from the conversion above is: ", cartesianToPolar(x, y))
    


else:
    print("You are about to convert from Polar coordinates to Cartesian Coordinates")
    while True:
        try:
            time.sleep(1)
            r = float(input("Enter the length of the line (r): "))
            if r == 0:
                print("Enter a value more than 0")
            else:
                print("r input received successfully! Now enter Θ ")
                break;
        except ValueError:
            print("Enter a numeric value!")
            continue
    while True:
        try:
            time.sleep(1)
            angle = float(input("Enter the angle (Θ): "))
            if angle == 0:
                print("Enter a value more than 0")
            else:
                print("Θ input received successfully! ")
                break;
        except ValueError:
            print("Enter a numeric value!")
            continue
    print(r, angle)
    
    time.sleep(1)
    
    # Function to convert from Polar to Cartesian
    def polarToCartesian(r, angle):
        # We will use the sine and cosine rules to get x,y
        angle = math.radians(angle)
        sin = math.sin(angle)
        cos = math.cos(angle)
        x = r*cos
        x = round(x, 2)
        y = r*sin
        y = round(y, 2)
        
        cartesian = x, y
        return cartesian
    
    polarToCartesian(r, angle)
    print("Conversion has been successful!")
    time.sleep(1)
    print("The results obtained from the conversion above is: ", polarToCartesian(r, angle))
    
    # while True:
    #     try:
    #         print("You are about to convert from Cartesian to Polar. Enter x and y coordinate pair")
    #         time.sleep(1)
    #         y = float(input("Enter the y value : "))
    #         if y == 0:
    #             print("Enter a value more than 0")
    #         else:
    #             print("y input received successfully!")
    #             exit;
    #     except ValueError:
    #         print("Enter a numeric value!")
    #         continue
        
        
# Now we have the relevant values: