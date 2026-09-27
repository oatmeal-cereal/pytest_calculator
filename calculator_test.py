import pytest
from calculator import Calculator

@pytest.fixture
def calc():
    return Calculator()

def test_add(calc):
    assert calc.add(3, 4) == 7
    assert calc.add(2, 2) == 3

def test_sub(calc):
    assert calc.subtract(6, 3) == 3

def test_mult(calc):
    assert calc.multiply(4, 4) == 16

def test_divide(calc):
    assert calc.divide(3, 1) == 3