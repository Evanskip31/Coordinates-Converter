# This is a script that converts coordinates from whichever format - Welcome!
# import time - this will be used especially during time sleep
import time

# Let's print the purpose text
print("You are about to convert coordinates from one format to another, or one system to another!")
time.sleep(2)
# We can list the options available for conversion
options1 = 'Degrees Minutes Seconds to Decimal Degrees as option 1' 
options2 = 'Degrees Minutes Seconds to Degrees Decimal Minutes'
options3 = 'Decimal Degrees to Degrees Minutes Seconds'
options4 = 'Decimal Degrees to Degrees Demimal Minutes'
options5 = 'Degrees Minutes Seconds to UTM'
option6 = 'UTM to Degrees Minutes Seconds'

list = ['Degrees Minutes Seconds to Decimal Degrees', 
        'Degrees Minutes Seconds to Degrees Decimal Minutes', 
        'Decimal Degrees to Degrees Minutes Seconds', 
        'Decimal Degrees to Degrees Demimal Minutes', 
        'Degrees Minutes Seconds to UTM', 
        'UTM to Degrees Minutes Seconds'
       ]
num_list = [1, 2, 3, 4, 5, 6]
n = 1
# for loop to place the list in a numbered order
for each in list:
    time.sleep(1)
    print("Option", n, ":", each)
    n += 1
# Now we are set to start, shall we?
# Let's use an example like 30° 30' 15"
# To note: 1° = 60' = 3600" and so 1' = 60"
d = 30
m = 15
s = 30

# 1' = 60''
s = s/60
m = (m + s)
# print(m)
m = m/60

# print(d+round(m, 5))
# print(options1)
# using while loop to check for consistency and validation
while True:
    time.sleep(1)
    try:
        option = int(input('Enter an Option from the above list: '))
        if option in num_list:
            print("Input received successfully!")
            break
        else:
            print("Enter a valid option from the list above!")
    except ValueError:
        print("Enter a numeric value! Choose between 1 to 6")
        continue
    
# Now we have the available option to perform our conversions
# Remember this can be the first approach to do it. Another is to make inputs for users i.e what 
# coordinate format do you want to change from, to change to?


if option == 1:
    time.sleep(1)
    print("You are about to convert from", list[0])
    # Keep in mind that we are converting from degrees minutes and seconds to decimal degrees
    # so first we ask for input differently degrees, minutes and seconds
    time.sleep(1)
    # Let's obtain latitude and longitude from the user
    print("Please Enter DDDMMSS in that order with no space, hyphen or comma")
    while True:
        try:
            latitude = int(input("Enter the latitude: "))
            time.sleep(1)
            # Check if coordinates lat start with zero. If so, automatically it will be ignored, thus leaving 6 chars
            if len(str(latitude)) == 6:
                latitude = str(0) + str(latitude)
            #  Change the input to str to be able to slice through input, then do a validation for each slice.
            
            # for degrees
            first_three = str(latitude)
            first_three = first_three[0:3]
            
            # for minutes
            mid_two = str(latitude)
            mid_two = mid_two[3:5]
                        
            # for seconds
            last_two = str(latitude)
            last_two = last_two[5:7]
            
            # if conditions to check for validations
            if len(str(latitude)) != 7:
                print("Please check that you entered all the characters well! Use this format DDDMMSS")
            elif int(first_three) > 360:
                print("You entered", first_three+"°", "which is more than 360°! Enter something between 0 and 360, both inclusive!")
            elif int(mid_two) > 60:
                print("You entered", mid_two+"'", "which is more than 60' (minutes)! Enter something between 0 and 60, both inclusive!")
            elif int(last_two) > 60:
                print("You entered", last_two+'"', 'which is more than 60" (seconds)! Enter something between 0 and 60, both inclusive!')
            elif latitude == 0000000:
                print('Enter a valid value! 0° cannot be converted!')
            
            else:
                print("Your input has been saved successfully. Now enter orientation as North(N) or South(S)")
                time.sleep(1)
                
                # Input for orientation as either N(North) or S(South)
                while True:
                    try:
                        lat_position = str(input("Enter Orientation as either N or S: "))
                        if lat_position == 'N' or lat_position == 'S':
                            print("Input received successfully!")
                            break
                        else:
                            print("Enter a valid option as North(N) or South(S)")
                    except ValueError:
                        print("Please Enter a Valid Option!")
                        continue
                break;
        except ValueError:
            print("Please Enter only numbers! No letters, special characters or spaces")
            continue
        
        # Now it is time for longitude
    while True:
        try:
            longitude = int(input("Enter the longitude: "))
            time.sleep(1)
            # Check if coordinates lat start with zero. If so, automatically it will be ignored, thus leaving 6 chars
            if len(str(longitude)) == 6:
                longitude = str(0) + str(longitude)
            #  Change the input to str to be able to slice through input, then do a validation for each slice.
            
            # for degrees
            ln_first_three = str(longitude)
            ln_first_three = ln_first_three[0:3]
            
            # for minutes
            ln_mid_two = str(longitude)
            ln_mid_two = ln_mid_two[3:5]
            
            # for seconds
            ln_last_two = str(longitude)
            ln_last_two = ln_last_two[5:7]
            
            # latitude = str(latitude)
            if len(str(longitude)) != 7:
                print("Please check that you entered all the characters well! Use this format DDDMMSS")
            elif int(ln_first_three) > 360:
                print("You entered", ln_first_three+"°", "which is more than 360°! Enter something between 0 and 360, both inclusive!")
            elif int(ln_mid_two) > 60:
                print("You entered", ln_mid_two+"'", "which is more than 60' (minutes)! Enter something between 0 and 60, both inclusive!")
            elif int(ln_last_two) > 60:
                print("You entered", ln_last_two+"''", "which is more than 60'' (seconds)! Enter something between 0 and 60, both inclusive!")
            elif longitude == 0000000:
                print('Enter a valid value! 0° cannot be converted!')
            
            else:
                print("Your input has been saved successfully. Now enter orientation as East(E) or West(W)")
                time.sleep(1)
                
                # Input for orientation as either E(East) or W(West)
                while True:
                    try:
                        lon_position = str(input("Enter Orientation as either E or W: "))
                        if lon_position == 'E' or lon_position == 'W':
                            print("Input received successfully!")
                            break
                        else:
                            print("Enter a valid option as East(E) or West(W)")
                    except ValueError:
                        print("Please Enter a Valid Option!")
                        continue
                break;
        except ValueError:
            print("Please Enter only numbers! No letters, special characters or spaces")
            continue


    # Now we have lats and long, validated enough to return real results
    time.sleep(1)
    print("You have entered", first_three+"°", mid_two+"'", last_two+'"', lat_position)
    print("You have entered", ln_first_three+"°", ln_mid_two+"'", ln_last_two+'"', lon_position)
    #verify for correctness of your input -> Coming Soon!
    
    # This is where the computation will be
    def calculateNow():
        # changing from DMS to DD
        # changing latitude
        sec_to_min = int(last_two)/60
        mins = int(mid_two) + sec_to_min
        min_to_deg = mins/60
        lat_dec_deg = int(first_three) + min_to_deg
        lat_dec_deg = round(lat_dec_deg, 4)
        print(lat_dec_deg)
        lat_dec_deg = str(lat_dec_deg) # changing to str
        #changing longitude
        sec_to_min = int(ln_last_two)/60
        mins = int(ln_mid_two) + sec_to_min
        min_to_deg = mins/60
        lon_dec_deg = int(ln_first_three) + min_to_deg
        lon_dec_deg = round(lon_dec_deg, 4)
        print(lon_dec_deg)
        lon_dec_deg = str(lon_dec_deg) # changing to str
        return lat_dec_deg+"° "+ lat_position, lon_dec_deg+"° "+ lon_position 
    conversion_1 = calculateNow()
    time.sleep(1)
    print("The results of your conversion above are", conversion_1)
    
    

if option == 2:
    time.sleep(1)
    print("You are about to convert from", list[1])
    # Keep in mind that we are converting from degrees minutes and seconds to degrees decimal minutes
    # so first we ask for input differently degrees, minutes and seconds
    time.sleep(1)
    # Let's obtain latitude and longitude from the user
    print("Please Enter DDDMMSS in that order with no space, hyphen or comma")
    while True:
        try:
            latitude = int(input("Enter the latitude: "))
            time.sleep(1)
            # Check if coordinates lat start with zero. If so, automatically it will be ignored, thus leaving 6 chars
            if len(str(latitude)) == 6:
                latitude = str(0) + str(latitude)
            #  Change the input to str to be able to slice through input, then do a validation for each slice.
            
            # for degrees
            first_three = str(latitude)
            first_three = first_three[0:3]
            
            # for minutes
            mid_two = str(latitude)
            mid_two = mid_two[3:5]
            
            # This is where the computation will be
            
            # for seconds
            last_two = str(latitude)
            last_two = last_two[5:7]
            
            # if conditions to check for validations
            if len(str(latitude)) != 7:
                print("Please check that you entered all the characters well! Use this format DDDMMSS")
            elif int(first_three) > 360:
                print("You entered", first_three+"°", "which is more than 360°! Enter something between 0 and 360, both inclusive!")
            elif int(mid_two) > 60:
                print("You entered", mid_two+"'", "which is more than 60' (minutes)! Enter something between 0 and 60, both inclusive!")
            elif int(last_two) > 60:
                print("You entered", last_two+'"', 'which is more than 60" (seconds)! Enter something between 0 and 60, both inclusive!')
            elif latitude == 0000000:
                print('Enter a valid value! 0° cannot be converted!')
            
            else:
                print("Your input has been saved successfully. Now enter orientation as North(N) or South(S)")
                time.sleep(1)
                
                # Input for orientation as either N(North) or S(South)
                while True:
                    try:
                        lat_position = str(input("Enter Orientation as either N or S: "))
                        if lat_position == 'N' or lat_position == 'S':
                            print("Input received successfully!")
                            break
                        else:
                            print("Enter a valid option as North(N) or South(S)")
                    except ValueError:
                        print("Please Enter a Valid Option!")
                        continue
                break;
        except ValueError:
            print("Please Enter only numbers! No letters, special characters or spaces")
            continue
        
        # Now it is time for longitude
    while True:
        try:
            longitude = int(input("Enter the longitude: "))
            time.sleep(1)
            # Check if coordinates lat start with zero. If so, automatically it will be ignored, thus leaving 6 chars
            if len(str(longitude)) == 6:
                longitude = str(0) + str(longitude)
            #  Change the input to str to be able to slice through input, then do a validation for each slice.
            
            # for degrees
            ln_first_three = str(longitude)
            ln_first_three = ln_first_three[0:3]
            
            # for minutes
            ln_mid_two = str(longitude)
            ln_mid_two = ln_mid_two[3:5]
            
            # for seconds
            ln_last_two = str(longitude)
            ln_last_two = ln_last_two[5:7]
            
            # latitude = str(latitude)
            if len(str(longitude)) != 7:
                print("Please check that you entered all the characters well! Use this format DDDMMSS")
            elif int(ln_first_three) > 360:
                print("You entered", ln_first_three+"°", "which is more than 360°! Enter something between 0 and 360, both inclusive!")
            elif int(ln_mid_two) > 60:
                print("You entered", ln_mid_two+"'", "which is more than 60' (minutes)! Enter something between 0 and 60, both inclusive!")
            elif int(ln_last_two) > 60:
                print("You entered", ln_last_two+"''", "which is more than 60'' (seconds)! Enter something between 0 and 60, both inclusive!")
            elif longitude == 0000000:
                print('Enter a valid value! 0° cannot be converted!')
            
            else:
                print("Your input has been saved successfully. Now enter orientation as East(E) or West(W)")
                time.sleep(1)
                
                # Input for orientation as either E(East) or W(West)
                while True:
                    try:
                        lon_position = str(input("Enter Orientation as either E or W: "))
                        if lon_position == 'E' or lon_position == 'W':
                            print("Input received successfully!")
                            break
                        else:
                            print("Enter a valid option as East(E) or West(W)")
                    except ValueError:
                        print("Please Enter a Valid Option!")
                        continue
                break;
        except ValueError:
            print("Please Enter only numbers! No letters, special characters or spaces")
            continue


    # Now we have lats and long, validated enough to return real results
    time.sleep(1)
    print("You have entered", first_three+"°", mid_two+"'", last_two+'"', lat_position)
    print("You have entered", ln_first_three+"°", ln_mid_two+"'", ln_last_two+'"', lon_position)
    #verify for correctness of your input -> Coming Soon!
    
    # This is where the computation will be
    def calculateToDDM():
        # changing from DMS to DDM
        # converting latitude
        lat_sec_to_min = int(last_two)/60
        lat_dec_min = int(mid_two) + lat_sec_to_min
        lat_dec_min = round(lat_dec_min, 4)
        lat_deg_dec_min = first_three + '°' + ' ' + str(lat_dec_min) + "' "
        print(lat_deg_dec_min)
        # converting logitude
        lon_sec_to_min = int(ln_last_two)/60
        lon_dec_min = int(ln_mid_two) + lon_sec_to_min
        lon_dec_min = round(lon_dec_min, 4)
        lon_deg_dec_min = ln_first_three + '°' + ' ' + str(lon_dec_min) + "' "
        print(lon_deg_dec_min)
        return lat_deg_dec_min + lat_position, lon_deg_dec_min + lon_position
    dmsToddm = calculateToDDM()
    time.sleep(1)
    print("The results of your conversion above are", dmsToddm)
   
    # Converting from Decimal Degrees to Degrees Minutes Seconds
elif option == 3:
    time.sleep(1)
    input_lat = ''
    # Loop to enter latitude
    while True:
        
        def inputValues():
            global input_lat
            # Enter latitude
            latitude = str(input("Enter Latitude: "))
            inputValues.orientation_lt = ''
            # Separate the sign(-) if it exists
            time.sleep(1)
            for i, index in zip(latitude, range(len(latitude))):
                if index == 0 and i == '-':
                    inputValues.orientation_lt = 'S'
                elif index == 0 and i != '-':
                    inputValues.orientation_lt = 'N' 
                    input_lat = latitude
                
                else:
                    input_lat = latitude
            
            return inputValues.orientation_lt
        # Function callback
        inputValues()
        orientation_lt = inputValues.orientation_lt
        time.sleep(1)
        # Function that is used to validate input entered.
        def validNum():
            while True:
                # Validating input entered. Should not be 0 or more than 360.
                validNum.lat_numeric = float(input_lat)
                print(validNum.lat_numeric)
                try: 
                    if validNum.lat_numeric > 360 or validNum.lat_numeric == 0 or validNum.lat_numeric < -360:
                        print("Enter coordinates between the range of 0 and 360 or 0 and -360, both inclusive")
                        time.sleep(1)
                        inputValues()
                        #break
                    else:
                        print("Input received successfully!")
                         
                        break
                except ValueError:
                    print("Enter a valid value!")
                    continue
                    inputValues()
        
        # This section is used to ensure numbers were entered and not letters or other characters
        plain = 0
        if input_lat[0] == '-':
            input_lat = input_lat[1:]
        try:
            for i in input_lat:
                if i == '.':
                    pass
                else:
                    plain += int(i)
                    
            validNum()
            break
        except ValueError:
            print("You entered invalid characters. No letters! i.e -125.45 or 90.3455")
            time.sleep(1)
            continue
            inputValues()
            
        
        
    final_Lt_value = validNum.lat_numeric
    print(final_Lt_value)
    
    time.sleep(1)
    input_lon = ''
    # Loop to enter longitude
    while True:
        
        def inputLonValues():
            global input_lon
            # Enter longitude
            longitude = str(input("Enter Longitude: "))
            inputLonValues.orientation_ln = ''
            # Separate the sign(-) if it exists
            time.sleep(1)
            for i, index in zip(longitude, range(len(longitude))):
                if index == 0 and i == '-':
                    print("Lon is negative!")
                    inputLonValues.orientation_ln = 'W'
                elif index == 0 and i != '-':
                    inputLonValues.orientation_ln = 'E'
                    print("Lon is positive!") 
                    input_lon = longitude
                
                else:
                    input_lon = longitude
            
            return inputLonValues.orientation_ln
        # Function callback
        inputLonValues()
        orientation_ln = inputLonValues.orientation_ln
        time.sleep(1)
        # Function that is used to validate input entered.
        def validLnNum():
            while True:
                # Validating input entered. Should not be 0 or more than 360.
                validLnNum.lon_numeric = float(input_lon)
                print(validLnNum.lon_numeric)
                try: 
                    if validLnNum.lon_numeric > 360 or validLnNum.lon_numeric == 0 or validLnNum.lon_numeric < -360:
                        print("Enter coordinates between the range of 0 and 360 or 0 and -360, both inclusive")
                        time.sleep(1)
                        inputLonValues()
                        #break
                    else:
                        print("Input received successfully!")
                        break
                except ValueError:
                    print("Enter a valid value!")
                    continue
                    inputLonValues()
        
        # This section is used to ensure numbers were entered and not letters or other characters
        plain = 0
        if input_lon[0] == '-':
            input_lon = input_lon[1:]
        try:
            for i in input_lon:
                if i == '.':
                    pass
                else:
                    plain += int(i)
                    
            validLnNum()
            break
        except ValueError:
            print("You entered invalid characters. No letters! i.e -125.45 or 90.3455")
            time.sleep(1)
            continue
            inputLonValues()
            
        
        
    final_Ln_value = validLnNum.lon_numeric
    print(final_Ln_value)
    time.sleep(1)
    # Now we have working values. We can start the conversion
    def convertToDMS():
        # let's convert to string so we can split
        # Latitude
        latitude_to_string = str(final_Lt_value)
        lat_split = latitude_to_string.split(".")
        lat_deg = lat_split[0]+'°'
        lat_dec = lat_split[1]
        len_lat_dec = len(lat_dec)
        lat_int = int(lat_dec)
        to_mins = (lat_int/(10**len_lat_dec))*60
        mins_to_string = str(to_mins)
        mins_split = mins_to_string.split(".")
        lat_min = mins_split[0]+"'"
        min_dec = mins_split[1]
        len_min_dec = len(min_dec)
        min_int = int(min_dec)
        to_secs= (min_int/(10**len_min_dec))*60
        to_secs = round(to_secs, 2)
        to_secs = str(to_secs)+'"'
        
        print(lat_deg, lat_min, to_secs)
    
        # convert to integer for calculations
        
        # Longitude
        longitude_to_string = str(final_Ln_value)
        lon_split = longitude_to_string.split(".")
        lon_deg = lon_split[0]+'°'
        lon_dec = lon_split[1]
        len_lon_dec = len(lon_dec)
        lon_int = int(lon_dec)
        to_mins_ln = (lon_int/(10**len_lon_dec))*60
        mins_to_ln_string = str(to_mins_ln)
        mins_ln_split = mins_to_ln_string.split(".")
        lon_min = mins_ln_split[0]+"'"
        min_ln_dec = mins_ln_split[1]
        len_min_ln_dec = len(min_ln_dec)
        min_ln_int = int(min_ln_dec)
        to_ln_secs= (min_ln_int/(10**len_min_ln_dec))*60
        to_ln_secs = round(to_ln_secs, 2)
        to_ln_secs = str(to_ln_secs)+'"'
        print(lon_deg, lon_min, to_ln_secs)
        #return lat_deg+"° "+ str(lat_min)+"'"+ str(to_secs)+'" ', lon_deg+"° "+ str(lon_min)+"' "+ str(to_ln_secs)+'"'
        print("The results of your conversion is", lat_deg, lat_min, to_secs, orientation_lt, "and", lon_deg, lon_min, to_ln_secs, orientation_ln)
    
    convertToDMS()
            
elif option == 4:
    time.sleep(1)
    input_lat = ''
    # Loop to enter latitude
    while True:
        
        def inputValues():
            global input_lat
            # Enter latitude
            latitude = str(input("Enter Latitude: "))
            inputValues.orientation_lt = ''
            # Separate the sign(-) if it exists
            time.sleep(1)
            for i, index in zip(latitude, range(len(latitude))):
                if index == 0 and i == '-':
                    inputValues.orientation_lt = 'S'
                elif index == 0 and i != '-':
                    inputValues.orientation_lt = 'N' 
                    input_lat = latitude
                
                else:
                    input_lat = latitude
            
            return inputValues.orientation_lt
        # Function callback
        inputValues()
        orientation_lt = inputValues.orientation_lt
        time.sleep(1)
        # Function that is used to validate input entered.
        def validNum():
            while True:
                # Validating input entered. Should not be 0 or more than 360.
                validNum.lat_numeric = float(input_lat)
                print(validNum.lat_numeric)
                try: 
                    if validNum.lat_numeric > 360 or validNum.lat_numeric == 0 or validNum.lat_numeric < -360:
                        print("Enter coordinates between the range of 0 and 360 or 0 and -360, both inclusive")
                        time.sleep(1)
                        inputValues()
                        #break
                    else:
                        print("Input received successfully!")
                         
                        break
                except ValueError:
                    print("Enter a valid value!")
                    continue
                    inputValues()
        
        # This section is used to ensure numbers were entered and not letters or other characters
        plain = 0
        if input_lat[0] == '-':
            input_lat = input_lat[1:]
        try:
            for i in input_lat:
                if i == '.':
                    pass
                else:
                    plain += int(i)
                    
            validNum()
            break
        except ValueError:
            print("You entered invalid characters. No letters! i.e -125.45 or 90.3455")
            time.sleep(1)
            continue
            inputValues()
            
        
        
    final_Lt_value = validNum.lat_numeric
    print(final_Lt_value)
    
    time.sleep(1)
    input_lon = ''
    # Loop to enter longitude
    while True:
        
        def inputLonValues():
            global input_lon
            # Enter longitude
            longitude = str(input("Enter Longitude: "))
            inputLonValues.orientation_ln = ''
            # Separate the sign(-) if it exists
            time.sleep(1)
            for i, index in zip(longitude, range(len(longitude))):
                if index == 0 and i == '-':
                    print("Lon is negative!")
                    inputLonValues.orientation_ln = 'W'
                elif index == 0 and i != '-':
                    inputLonValues.orientation_ln = 'E'
                    print("Lon is positive!") 
                    input_lon = longitude
                
                else:
                    input_lon = longitude
            
            return inputLonValues.orientation_ln
        # Function callback
        inputLonValues()
        orientation_ln = inputLonValues.orientation_ln
        time.sleep(1)
        # Function that is used to validate input entered.
        def validLnNum():
            while True:
                # Validating input entered. Should not be 0 or more than 360.
                validLnNum.lon_numeric = float(input_lon)
                print(validLnNum.lon_numeric)
                try: 
                    if validLnNum.lon_numeric > 360 or validLnNum.lon_numeric == 0 or validLnNum.lon_numeric < -360:
                        print("Enter coordinates between the range of 0 and 360 or 0 and -360, both inclusive")
                        time.sleep(1)
                        inputLonValues()
                        #break
                    else:
                        print("Input received successfully!")
                        break
                except ValueError:
                    print("Enter a valid value!")
                    continue
                    inputLonValues()
        
        # This section is used to ensure numbers were entered and not letters or other characters
        plain = 0
        if input_lon[0] == '-':
            input_lon = input_lon[1:]
        try:
            for i in input_lon:
                if i == '.':
                    pass
                else:
                    plain += int(i)
                    
            validLnNum()
            break
        except ValueError:
            print("You entered invalid characters. No letters! i.e -125.45 or 90.3455")
            time.sleep(1)
            continue
            inputLonValues()
            
        
        
    final_Ln_value = validLnNum.lon_numeric
    print(final_Ln_value)
    time.sleep(1)
    # Now we have working values. We can start the conversion
    def convertToDDM():
        # convert latitudes
        latitude_to_string = str(final_Lt_value)
        lat_split = latitude_to_string.split(".")
        lat_deg = lat_split[0]+'°'
        lat_dec = lat_split[1]
        len_lat_dec = len(lat_dec)
        lat_int = int(lat_dec)
        to_mins = round((lat_int/(10**len_lat_dec))*60, 5)
        lat_min = str(to_mins)+"'"
        
        # convert longitudes
        longitude_to_string = str(final_Ln_value)
        lon_split = longitude_to_string.split(".")
        lon_deg = lon_split[0]+'°'
        lon_dec = lon_split[1]
        len_lon_dec = len(lon_dec)
        lon_int = int(lon_dec)
        to_mins_ln = round((lon_int/(10**len_lon_dec))*60, 5)
        mins_to_ln_string = str(to_mins_ln)
        lon_min = mins_to_ln_string+"'"
        
        print("The results of your conversion is", lat_deg, lat_min, orientation_lt, "and", lon_deg, lon_min, orientation_ln)
        
    convertToDDM()
        
elif option == 5:
    time.sleep(1)
    print("You are about to convert from", list[4])
elif option == 6:
    time.sleep(1)
    print("You are about to convert from", list[5])
