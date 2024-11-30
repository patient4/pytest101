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
