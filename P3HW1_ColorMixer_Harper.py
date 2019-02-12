# CTI-110 
# P3HW1 - Color Mixer 
# Jordan Harper
# 13 Febuary 2019
#
#
# Input two primary colors
# Display the results if they make a secondary color.
# If not show a error message
# 
#



#red = 1
#yellow = 2
#blue = 3
#purple = 4
#green = 5
#orange = 6

# Gets two primary colors

print('The following colors are represented by numbers.')
print('Which then determine the secondary color')
print('1 = red 2 = yellow and 3=blue')
primarycolor1 = int(input('Enter number for the first Primary color: '))
primarycolor2 = int(input('Enter number for the second Primary color: '))

# If the two primary colors equal a value then the message will be displayed If not it will record a error.
if primarycolor1 + primarycolor2 == 3:
    print('The secondary color will be orange')
elif primarycolor1 + primarycolor2 == 4:
    print('The secondary color will be purple')

elif primarycolor1 + primarycolor2 == 5:
    print('The secondary color will be Green')

else:
    print('The following Colors do not create a secondary solor.')



        



       
    

