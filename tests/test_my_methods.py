# This file will conatin all my test cases realated to my_methods.py
# simply import the methods from the package

import pytest
import source.my_methods as methods


# notice how there is test_ in the test name this is the auto discovery of tests in pytest
# Whenevery we write test cases in pytest we have to provide the test methods with 'test' in the name
def test_add():
    a = 4
    b = 1
    expected = 5 # we expect that the method add should return 5 if a =4 and b = 1
    actual = methods.add(a,b) # calling the method
    assert actual == expected # asserting that the method is working as expected.

def test_subtract():
    b = 10
    a = 5
    expected = -5
    actual = methods.subtract(a,b)
    assert actual == expected

def test_multiply():
    a = 10
    b = 10
    expected = 100
    actual = methods.multiply(a,b)
    assert actual == expected

def test_divide():
    a = 100
    b = 10
    expected = 10
    actual = methods.divide(a,b)
    assert actual == expected

# write a test that will test that ZeroDivisonError
def test_zero_division():
    with pytest.raises(ZeroDivisionError):
        methods.divide(10, 0)

