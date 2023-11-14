"""Intro To Object Oriented Programming."""
from __future__ import annotations

__author__ = "730705343"


class Point:
    """Setting the attributes for the class."""
    x: float
    y: float

    def __init__(self, x_init: float, y_init: float):
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