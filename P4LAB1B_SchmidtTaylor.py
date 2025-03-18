import turtle
wn = turtle.Screen()      # Creates a playground for turtles
taylor = turtle.Turtle()    # Create a turtle, assign to Taylor
taylor.shape("turtle")
taylor.color("hotpink")
taylor.pensize(4)
taylor.speed(3)

#Code for the letter T
taylor.forward(55)  
taylor.back(26)
taylor.right(90)
taylor.forward(55)

#Move the turtle over
taylor.penup()
taylor.left(90)
taylor.forward(55)
taylor.pendown()

# Draw an S from bottom to top
taylor.circle(14, 170)   # Lower curve (counterclockwise)
taylor.circle(-14, 170)  # Upper curve (clockwise)

# end commands
wn.mainloop()