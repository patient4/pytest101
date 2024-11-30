"""
This module will contain the Circle class logic
this will extend the base class Shape and implement the Area() and Perimeter() methods
"""
import math

from source.shape import Shape


class Circle(Shape):
    def __init__(self, radius):
        super().__init__()
        self.radius = radius
    def area(self):
        return math.pi * self.radius ** 2
    def perimeter(self):
        return 2 * math.pi * self.radius

