"""EX05_turtle_scene - 'Minecraft Sunset at The Cherry Blossoms'.

Above and Beyond(Section 8): Something I did that I thought was interesting was using the .circle() function to draw pebbles on the ground
"""

__author__ = "730705343"

from turtle import Turtle, done 
art: Turtle = Turtle()


def main() -> None:
    """Entryway into the main turtle drawing."""
    art.speed(0)
    sky(art, -400, -400)
    tree_leaves(art, -200, 25)
    tree_trunk(art, -150, -100)
    sunset(art, 100, 100)
    inside_sunset(art, 125, 125)
    ground(art, -400, -100)
    tree_leaves(art, -50, 25)
    tree_trunk(art, 0, -100)
    pebbles(art, -100, -150)
    pebbles(art, -150, -170)
    pebbles(art, -125, -140)
    pebbles(art, 0, -150)
    pebbles(art, -20, -200)
    pebbles(art, -50, -160)
    done()


def tree_leaves(art: Turtle, xcoord: float, ycoord: float) -> None:
    """Draw the leaves of a tree."""
    art.begin_fill()
    art.color("pink")
    art.penup()
    art.goto(xcoord, ycoord)
    art.pendown()
    art.begin_fill()
    art.forward(75)
    art.right(90)
    art.forward(25)
    art.left(90)
    art.forward(25)
    art.right(90)
    art.forward(25)
    art.right(90)
    art.forward(125)
    art.right(90)
    art.forward(25)
    art.right(90)
    art.forward(25)
    art.left(90)
    art.forward(25)
    art.end_fill()


def tree_trunk(art: Turtle, xcoord: float, ycoord: float) -> None:
    """Draws the tree trunk of the tree."""
    art.begin_fill()
    art.color("brown")
    art.penup()
    art.goto(xcoord, ycoord)
    art.pendown()
    art.forward(75)
    art.left(90)
    art.forward(25)
    art.left(90)
    art.forward(75)
    art.left(90)
    art.forward(25)
    art.end_fill()


def sunset(art: Turtle, xcoord: float, ycoord: float) -> None:
    """Draws the minecraft sun setting."""
    art.begin_fill()
    art.color("orange")
    art.penup()
    art.goto(xcoord, ycoord)
    art.pendown()
    # creating a while loop to simplify the code
    i: int = 0
    while i < 4:
        art.forward(150)
        art.left(90)
        i += 1
    art.end_fill()


def inside_sunset(art: Turtle, xcoord: float, ycoord: float) -> None:
    """Draws the yellow shade of the sun."""
    art.begin_fill()
    art.penup()
    art.color("yellow")
    art.goto(xcoord, ycoord)
    art.pendown()
    i: int = 0
    # creating a while loop to simplify the code
    while i < 4:
        art.forward(100)
        art.left(90)
        i += 1
    art.end_fill()


def sky(art: Turtle, xcoord: float, ycoord: float) -> None:
    """Draws sky background."""
    art.begin_fill()
    art.penup()
    art.color("lightblue")
    art.goto(xcoord, ycoord)
    art.pendown()
    i: int = 0
    while i < 4:
        art.forward(800)
        art.left(90)
        i += 1
    art.end_fill()


def ground(art: Turtle, xcoord: float, ycoord: float) -> None:
    """Draws the ground."""
    art.penup()
    art.begin_fill()
    art.color("green")
    art.goto(xcoord, ycoord)
    art.pendown()
    art.forward(800)
    art.right(90)
    art.forward(300)
    art.right(90)
    art.forward(800)
    art.right(90)
    art.forward(300)
    art.end_fill()
    art.right(90)


def pebbles(art: Turtle, xcoord: float, ycoord: float) -> None:
    """Grey dots meant to draw pebbles."""
    # this function is my above and beyond - implementing the circle function
    art.penup()
    art.begin_fill()
    art.color("grey")
    art.goto(xcoord, ycoord)
    art.pendown()
    art.circle(5)
    art.end_fill()


if __name__ == "__main__":
    main()