import source.Circle as Circle
import math
class TestCircle:

    def setup_method(self, method):
        print('setup')
        self.circle = Circle.Circle(10)
    def teardown_method(self, method):
        print('teardown')

    def test_area(self):
        assert self.circle.area() == math.pi * self.circle.radius ** 2

    def test_perimeter(self):
        assert self.circle.perimeter() == 2 * self.circle.radius * math.pi