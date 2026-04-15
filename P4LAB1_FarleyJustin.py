# Justin Farley
# 4/15/2026
# P4LAB1
# turtle graphics programs that draws a triangle and a square using loops

# Import Library
import turtle

# Create the turtle window and drawing object
win = turtle.Screen()
win.bgcolor("black")      # Set the window background color
win.title("P4LAB1")      # Set the window title
pen = turtle.Turtle()

# Set turtle options
pen.pensize(3)
pen.pencolor("orange")
pen.shape("arrow")

# Code to draw a square - ONLY WAY MY BRAIN CAN FIGURE OUT HOW TO DO IT! LOL
for side in range(4):
    pen.forward(100)
    pen.left(90)

pen.forward(100)
pen.left(90)
pen.forward(100)
pen.left(30)

#While loop that executes 2 times to draw the triangle on top of the square
sides = 2
while sides > 0:
    pen.forward(100)
    pen.left(120)
    sides = sides - 1

# Wait for user to close window
win.mainloop()
