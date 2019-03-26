# Calculates the conversion of pounds to kilograms
# 5 March 2019
# CTI-110 P4HW2 - Pounds to Kilograms table
# Jordan Harper
#
# Get pounds
# convert total kilograms
# display kilograms
# Get the total kilograms
def kilo_table():

    # Defined pounds in the range using start stop step format
    for pounds in range(100, 301, 10):
        
            
            # Enter the formula held in a variable format
            kilograms = pounds / 2.2046
            # Displays result specifically calling for 2 decimal places.
            print("{:.2f}".format(kilograms), 'kg')
            

           
kilo_table()

