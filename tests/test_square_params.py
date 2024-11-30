import pytest
import source.Square as square

# write a test function to test 4 area of squares using parametrize tests

""""
Basically there is this decorator we want to add observe the relation with the below defined method
The second param will imply as 
side = 1, expected = 1
side = 3, expected = 9.... so on 
this will trigger the len([(),()]) for here 4 tests.
"""
@pytest.mark.parametrize("side, expected", [(1, 1), (3, 9), (4,16), (100, 10000)])
def test_square_areas(side, expected):
    assert square.Square(side).area() == expected

@pytest.mark.parametrize("side, expected", [(1, 2), (3, 6), (4,8), (100, 200)])
def test_square_perimeters(side, expected):
    assert square.Square(side).perimeter() == expected