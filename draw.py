import turtle

# Create a turtle object
t = turtle.Turtle()

# Draw the face
t.circle(100)

# Draw the eyes
t.penup()
t.goto(-40, 120)
t.dot(20)
t.goto(40, 120)
t.dot(20)

# smile
t.goto(-40, 80)
t.pendown()
t.setheading(-60)
t.circle(50, 120)

# Keep the window open
turtle.done()
