from canvas import Canvas
from shapes import Square, Rectangle

# CLI Interface

# Canvas inputs
canvas_width = int(input("Enter canvas width: "))
canvas_height = int(input("Enter canvas height: "))

# Create instance for canvas color options, then provide accompanying input
canvas_color = input("Enter canvas color (white or black): ")
colors = {"white": (255, 255, 255), "black": (0, 0, 0)}

# Canvas Instance
canvas = Canvas(canvas_width, canvas_height, colors[canvas_color])

# We use the "while" loop so that the interface continues to ask the user if they would like to create more shapes
# until they offer the "quit" input.
while True:
    shape_type = input("What do you like to draw? Enter 'quit' to quit: ")

    # Use the ".lower" operator to force any capitalized user inputs to be lowercase.
    if shape_type.lower() == "rectangle":
        rec_x = int(input("Enter x coordinate for the rectangle: "))
        rec_y = int(input("Enter y coordinate for the rectangle: "))
        rec_w = int(input("Enter the width of the rectangle: "))
        rec_h = int(input("Enter the height of the rectangle: "))
        rec_r = int(input("Enter red intensity of the rectangle: "))
        rec_g = int(input("Enter green intensity of the rectangle: "))
        rec_b = int(input("Enter the blue intensity of the rectangle: "))
        r1 = Rectangle(x = rec_x, y = rec_y, height = rec_h, width = rec_w, color = (rec_r, rec_g, rec_b))
        r1.draw(canvas)

    if shape_type.lower() == "square":
        squ_x = int(input("Enter x coordinate for the square: "))
        squ_y = int(input("Enter y coordinate for the square: "))
        squ_s = int(input("Enter the side length of the square: "))
        squ_r = int(input("Enter red intensity of the square: "))
        squ_g = int(input("Enter green intensity of the square: "))
        squ_b = int(input("Enter blue intensity of the square: "))
        s1 = Square(x = squ_x, y= squ_y, side = squ_s, color = (squ_r, squ_g, squ_b))
        s1.draw(canvas)

    if shape_type == "quit":
        break

# Complete loop and create png file of canvas with shapes
canvas.make("draft1.png")
