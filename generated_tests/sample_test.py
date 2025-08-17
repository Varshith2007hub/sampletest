
import pytest
import math
from sample import Calculator, square, is_even

def test_add():
    calc = Calculator()
    assert calc.add(2, 3) == 5
    assert calc.add(-2, 3) == 1
    assert calc.add(0, 0) == 0

def test_divide():
    calc = Calculator()
    assert calc.divide(10, 2) == 5.0
    assert calc.divide(5, 1) == 5.0
    with pytest.raises(ValueError):
        calc.divide(10, 0)

def test_factorial():
    calc = Calculator()
    assert calc.factorial(0) == 1
    assert calc.factorial(5) == 120
    with pytest.raises(ValueError):
        calc.factorial(-1)

def test_square():
    assert square(2) == 4
    assert square(0) == 0
    assert square(-3) == 9

def test_is_even():
    assert is_even(2) == True
    assert is_even(1) == False
    assert is_even(0) == True
    assert is_even(-2) == True

