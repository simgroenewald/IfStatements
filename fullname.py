# Compulsory Task 2
fullname = input("Please enter your fullname:") # Allows user to enter name

if len(fullname) == 0:
    print("You haven't entered anything. Please enter your full name.")  # Returns message if user has not entered anything
if len(fullname) < 4 and len(fullname) >0:
    print("You have entered less than 4 characters. Please make sure that you have entered your name and surname") # Returns message if user has entered more than 0 characters and less than 4 characters
if len(fullname) > 25:
    print("You have entered more than 25 characters. Please make sure that you only entered your full name.") #Returns message if user has entered more than 25 characters
if len(fullname) > 4 and len(fullname) < 25:
    print("Thank you for entering your name.") # Returns this message if the if the name is longer than 4 characters and shorter than 25


          


