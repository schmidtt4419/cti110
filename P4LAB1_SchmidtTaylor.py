import turtle
wn = turtle.Screen()      # Creates a playground for turtles
taylor = turtle.Turtle()    # Create a turtle, assign to Taylor
taylor.shape("turtle")
taylor.color("hotpink")

for i in [0,1,2,3]:   # Loop for square
    taylor.forward(80)
    taylor.left(90)

taylor.left(180)    #Turns taylor around and moves her away from the origin
taylor.forward(80)

for i in [0,1,2]:        #Loop for triangle
    taylor.forward(80)
    taylor.right(120)

# end commands
wn.mainloop()             # Wait for user to close window