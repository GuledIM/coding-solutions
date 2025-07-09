year = int(input("Enter a year: "))

if year < 1582:
	print("Not within the Gregorian calendar period")
else:
    if year % 4 != 0: # Checks whether the year number isn't divisible by four, if not it's a common year
        print("Common year")
        
    elif year % 100 != 0: # Checks whether the year number isn't divisible by hundred, if not it's a leap year
        print("Leap year")
    
    elif year % 400 !=0: # Checks whether the year number isn't divisible by four hundred, if not it's a common year
        print("Common year")
    
    else: # For any other year number it's a common year
        print("Leap year")
        