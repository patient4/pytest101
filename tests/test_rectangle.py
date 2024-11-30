import source.Rectangle as rect

class TestRectangle:

    def setup_method(self):
        self.rect = rect.Rectangle(10,20)

    def test_area(self):
        assert self.rect.area() == self.rect.height * self.rect.width

    def test_perimeter(self):
        assert self.rect.perimeter() == 2 * (self.rect.width + self.rect.height)