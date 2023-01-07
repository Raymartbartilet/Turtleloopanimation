import turtle

# Set up the turtle
turtle.speed(0) # Set the turtle's speed to the maximum value
turtle.hideturtle() # Hide the turtle

# Set up the window
turtle.setup(800, 600) # Set the window size
turtle.bgcolor("black") # Set the background color

# Create a square that bounces around the screen
square_size = 50
square_color = "white"
x = 0
y = 0
dx = 2
dy = 2

while True:
    # Move the square
    x += dx
    y += dy

    # Change the direction of the square if it hits a wall
    if x > 400 - square_size / 2:
        dx = -2
    elif x < -400 + square_size / 2:
        dx = 2
    if y > 300 - square_size / 2:
        dy = -2
    elif y < -300 + square_size / 2:
        dy = 2

    # Clear the screen
    turtle.clear()

    # Draw the square
    turtle.penup()
    turtle.goto(x, y)
    turtle.pendown()
    turtle.color(square_color)
    for i in range(4):
        turtle.forward(square_size)
        turtle.right(90)

    # Update the screen
    turtle.update()

turtle.done()
