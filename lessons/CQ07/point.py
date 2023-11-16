"""Intro To Object Oriented Programming."""
from __future__ import annotations

__author__ = "730705343"


class Point:
    """Setting the attributes for the class."""
    x: float
    y: float

    def __init__(self, x_init: float = 0.0 , y_init: float = 0.0):
        """Assigning an initial value for x and y."""
        self.x = x_init
        self.y = y_init
    
    def scale_by(self, factor: int) -> None:
        """Mutates the points by updating the attributes."""
        self.x *= factor
        self.y *= factor

    def scale(self, factor: int) -> Point:
        """Creating a new point."""
        new_point: Point = Point(self.x * factor, self.y * factor)
        return new_point
    
    def __str__(self):
        """Prints out the points in a readable way."""
        return f"x: {self.x}; y: {self.y}"

    def __mul__(self, factor: int | float) -> Point:
        """Overloading the multiplication operator."""
        new_point: Point = Point(self.x * factor, self.y * factor)
        return new_point
    
    def __add__(self, value: int | float) -> Point:
        """Overloading the addition operator."""
        new_point: Point = Point(self.x + value, self.y + value)
        return new_point




    
    