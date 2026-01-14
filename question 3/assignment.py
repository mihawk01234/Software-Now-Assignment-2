import turtle

# --------------------------------------------------
# Recursive function to draw a single modified edge
# --------------------------------------------------


def draw_recursive_edge(length, depth):
    """
    Draws a line segment using recursion.

    depth = 0 → draw a straight line
    depth > 0 → divide the line into 3 parts and
                replace the middle part with an
                inward equilateral triangle
    """
    if depth == 0:
        # Base case: draw a straight line
        turtle.forward(length)
    else:
        # Divide the line into three equal segments
        length = length / 3

        # First segment
        draw_recursive_edge(length, depth - 1)

        # Create inward triangle indentation
        turtle.right(60)
        draw_recursive_edge(length, depth - 1)

        turtle.left(120)
        draw_recursive_edge(length, depth - 1)

        turtle.right(60)
        draw_recursive_edge(length, depth - 1)


# --------------------------------------------------
# Function to draw the initial polygon
# --------------------------------------------------
def draw_polygon(sides, length, depth):
    """
    Draws a regular polygon where each side
    is modified recursively.
    """
    angle = 360 / sides

    for _ in range(sides):
        draw_recursive_edge(length, depth)
        turtle.left(angle)


# --------------------------------------------------
# Main Program
# --------------------------------------------------
def main():
    # Get user input
    sides = int(input("Enter the number of sides: "))
    length = int(input("Enter the side length: "))
    depth = int(input("Enter the recursion depth: "))

    # Turtle setup
    turtle.speed(0)          # Fastest drawing speed
    turtle.hideturtle()      # Hide turtle cursor
    turtle.bgcolor("white")
    turtle.color("black")

    # Position turtle for better centering
    turtle.penup()
    turtle.goto(-length / 2, length / 3)
    turtle.pendown()

    # Draw the recursive polygon
    draw_polygon(sides, length, depth)

    # Keep the window open
    turtle.done()


# Run the program
main()
