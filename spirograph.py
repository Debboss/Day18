import turtle as t
import math

# Set up the screen
screen = t.Screen()
screen.bgcolor("white")

# Create a turtle
spiro_turtle = t.Turtle()
spiro_turtle.speed("fastest")
spiro_turtle.color("blue")

# Parameters for the spirograph
R = 100  # Radius of the large circle
r = 35   # Radius of the small circle
d = 75   # Distance from the center of the small circle to the drawing point

# Calculate the number of rotations for the small circle
rotations = R // math.gcd(R, r)

# Draw the spirograph
for _ in range(0, 360 * rotations + 1, 5):
    angle = math.radians(_)
    x = (R - r) * math.cos(angle) + d * math.cos((R - r) * angle / r)
    y = (R - r) * math.sin(angle) - d * math.sin((R - r) * angle / r)
    spiro_turtle.goto(x, y)

# Hide the turtle and display the result
spiro_turtle.hideturtle()
screen.exitonclick()
