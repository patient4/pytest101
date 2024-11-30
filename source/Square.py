# Write a class to override the area and perimeter of a square from Shape class.
# also implement param tests for 5 5 values for circle and perimeter tests.
from source.shape import Shape


class Square(Shape):
    def __init__(self, side):
        super().__init__()
        self.side = side

    def area(self):
        return self.side * self.side

    def perimeter(self):
        return 2 * self.side