# This program draws a square then a triangle.
# 20 February 2019
# CTI - 110 - P4T1A - Shapes
# Jordan Harper
#
# Import turtle for use in the program.
# execute the minimum facing movements.
# Have a loop finish the complete movement of a square.
# Remove pen from program so I can successfully move next start point.
# Repeat the following steps except creating a triangle instead of square.


# Starts the turtle function
import turtle
def main():
	# This function changes the size color and shape of the turtle
	turtle.pensize(5)            
	turtle.pencolor("red")     
	turtle.shape("turtle")

	# This uses a loop to repeat the movement steps twice for the turtle.
	for x in range(4):
		turtle.forward(50)
		turtle.right(90)

	# Pickups pen so a trail isn't left when moving to another section on screen
	turtle.penup()

	# Sets position of turtle to new location then puts pen back down 
	turtle.setpos(60,30)
	turtle.pendown()

	# Uses a loop 3 times to execute a triangle with the following steps
	for x in range(3):
		turtle.forward(100)          
		turtle.left(120) 
main()
    
   
