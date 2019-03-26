# This program draws a square then a triangle.
# 20 February 2019
# CTI - 110 - P4T1b - Initials
# Jordan Harper
#
# Import turtle to begin using function.
# Decide color size and any other Graffias that will be used.
# Use logic to decide how each move function should be used while using loops.
# The end result needs to end with the initials "JH" being displayed.


# Starts the turtle function
def main():
    import turtle

# This function changes the size color and shape of the turtle
    turtle.pensize(3)            
    turtle.pencolor("red")     
    turtle.shape("turtle")

# This sets the turtle at specific coordinates and begins moving in the pattern.
    turtle.setpos(0,0)
    turtle.forward(100)


# This picks the pin up, sets position at specific coordinates and then places pen back down to follow instructions
    turtle.penup()
    turtle.setpos(50,0)
    turtle.pendown()
    turtle.right(90)
    turtle.forward(100)


# This is a loop that does the following steps 3 times.
    for x in range(3):
        turtle.forward(50)
        turtle.right(90)


# Picks up pen, sets new coordinates, places pen and begins following written instructions.
    turtle.penup()
    turtle.setpos(105,0)
    turtle.pendown()
    turtle.right(90)
    turtle.forward(150)


# Picks up pen, sets new coordinates, places pen and begins following written instructions.
    turtle.penup()
    turtle.setpos(200,0)
    turtle.pendown()
    turtle.forward(150)


# Picks up pen, sets new coordinates, places pen and begins following written instructions.
    turtle.penup()
    turtle.setpos(200,-70)
    turtle.pendown()
    turtle.right(90)
    turtle.forward(100)

main()






