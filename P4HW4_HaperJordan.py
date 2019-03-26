# Uses a Nested Loop to create a shape using other shapes
# It then totals all positive integers
# 5 March 2019
# CTI-110 P4HW3 - Nested Loops
# Jordan Harper
#
#define the snowflake function
# moves and rotates a shape
# create the main shape inside a nested loop
# display the shape within shapes
#



# Starts the turtle function as well as rename turtle and pen color.
import turtle
t = turtle.Turtle()
t.pencolor('green')


def snowflake():

    # this first loop moves the shape a total of 10 times and then to the right 36 degrease
    for i in range(10):
        # This loop creates a pentagon
        for x in range(5):
            t.forward(100)
            t.left(72)
    # The if else statement states every other color will be red starting and ending with green.
        if i%2 == 0:
            t.pencolor('red')
        else:
            t.pencolor('green')
        t.right(36)
snowflake()
