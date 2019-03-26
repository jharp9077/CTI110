# takes input from user and uses the information to calculate the calories burned. 
# 26 February 2019
# CTI-110 P4HW1 - Calories Burned
# Jordan Harper
#
# Name and create a function
# Define a keep going variable for the while loop
# User inputs minutes they ran 
# Enter the variable calories_burned and set it to equal 5
# Create the statements minutes * calories burned to get the total
# Put the different possible outcomes in if elif statements and display outcomes
# create a else statement for any incorrect inputs
# Print thank you message a



# defined the function as calories burned.
d
ef calories_Burn():

    # Created the keep going variable and set to yes
    keep_going = 'yes'

    # added a while statement to the keep going variable 
    while keep_going == 'yes':

        # User inputs how many minutes they ran
        minutes = int(input('Enter how many minutes you ran either 20, 35, or 45. ', ))

        # Calories are permanently set to 5 since that his how much you'll burn on a treadmill.
        calories_burned = 5

        # If the user enters they used 20 minutes it goes through the following process.
        if minutes == 20:
            total_burn = calories_burned * minutes
            print("You have burned", total_burn, "calories.\n\n\n")
            keep_going = input("Do you want to keep going? Enter 'yes' , or 'no'. ", )

        # If the user enters they used 35 minutes it goes through the following process.
        elif minutes == 35:
            total_burn = calories_burned * minutes
            print("You have burned", total_burn, "calories.\n\n\n")
            keep_going = input("Do you want to keep going? Enter 'yes' , or 'no'. ", )

        # If the user enters they used 45 minutes it goes through the following process.
        elif minutes == 45:
            total_burn = calories_burned * minutes
            print("You have burned", total_burn, "calories.\n\n\n")
            keep_going = input("Do you want to keep going? Enter 'yes' , or 'no'. ", )

        # If the user uses none of the defined options it will use this process
        else:
            print('This is not a valid time you ran.\n\n\n')
            keep_going = input("Do you want to keep going? Enter 'yes' , or 'no'. ", )

    # Thanks the user with a message    
    print('Thanks for using our product')
calories_Burn()






     


    
