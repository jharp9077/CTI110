# This program tells the user which rectangle has the greater area or the same.
# 12 Febuary 2019 
# CTI-110 P3T1- Areas of Rectangles
# Jordan Harper
#

# Input the length and width of rectangle 1
# Input the length and width of rectangle 2
# Calculate the area of rectangle 1.
# Calculate the area of rectangle 2.
# if area1 > area2
#          Display ' Rectangle 1 has the greatest area."
# else if area2 > area1
#          Display 'Rectangle 2 has the greatest area."
# else
#          Display 'Both rectangles have the same area.'

#Get the dimentions of rectangle 1.

keep_going = "y"
while keep_going == 'y':

    length1= int(input('Enter the length of rectangle 1: '))
    width1 = int(input('Enter the width of rectangle 1: '))

# Get the dimentions of rectangle 2.
    length2= int(input('Enter the length of rectangle 2: '))
    width2 = int(input('Enter the width of rectangle 2: '))

# Calculate the areas of the rectangles
    area1 = length1 * width1
    area2 = length2 * width2

# Determines which has the gretest area.

    if area1 > area2:
        print('Rectangle 1 has the greater area.')

    elif area2 > area1:
        print('Rectangle 2 has the greater area.')
    else:
         print('Both have the same area.')

    keep_going = input('Do you want to calculate another' + \
                   'Rectangle (Enter Y for yes and N for no): ')
