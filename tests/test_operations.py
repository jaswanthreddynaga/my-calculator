import pytest
from calculator.operations import add, subtract, multiply, divide

# Unit Tests
def test_add():
    assert add(2, 3) == 5
    assert add(-1, 1) == 0
    assert add(0, 0) == 0

def test_subtract():
    assert subtract(5, 2) == 3
    assert subtract(10, 20) == -10
    assert subtract(0, 0) == 0

def test_multiply():
    assert multiply(2, 4) == 8
    assert multiply(-5, 5) == -25
    assert multiply(0, 100) == 0

def test_divide():
    assert divide(10, 2) == 5.0
    assert divide(5, 2) == 2.5

def test_divide_by_zero():
    with pytest.raises(ZeroDivisionError):
        divide(10, 0)

# Parameterized Tests
@pytest.mark.parametrize("num1, num2, expected", [
    (10, 5, 15),
    (-1, 1, 0),
    (0.1, 0.2, 0.3)
])
def test_add_parameterized(num1, num2, expected):
    assert add(num1, num2) == pytest.approx(expected)

@pytest.mark.parametrize("num1, num2, expected", [
    (10, 5, 5),
    (5, 10, -5),
    (0.5, 0.2, 0.3)
])
def test_subtract_parameterized(num1, num2, expected):
    assert subtract(num1, num2) == pytest.approx(expected)

# Add more parameterized tests for multiplication and division to ensure 100% coverage
@pytest.mark.parametrize("num1, num2, expected", [
    (2, 5, 10),
    (-2, 5, -10),
    (0.5, 4, 2)
])
def test_multiply_parameterized(num1, num2, expected):
    assert multiply(num1, num2) == pytest.approx(expected)

@pytest.mark.parametrize("num1, num2, expected", [
    (10, 2, 5.0),
    (1, 2, 0.5),
    (100, -10, -10.0)
])
def test_divide_parameterized(num1, num2, expected):
    assert divide(num1, num2) == pytest.approx(expected)