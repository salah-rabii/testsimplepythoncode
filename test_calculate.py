import pytest
# from code import addition, soustraction, multiplication, division
# import code
from calculate import addition, soustraction, multiplication, division
# import /Users/salah/Downloads/simple_code_python_for_test/code





def test_addition():
    assert addition(2, 3) == 7
    assert addition(-1, 1) == 0
    assert addition(0, 0) == 0

def test_soustraction():
    assert soustraction(9, 7) == 2
    assert soustraction(10, 4) == 6
    assert soustraction(0, 0) == 0

def test_multiplication():
    assert multiplication(2, 3) == 6
    assert multiplication(-1, 1) == -1
    assert multiplication(0, 5) == 0

def test_division():
    assert division(6, 2) == 3
    assert division(-6, 2) == -3
    assert division(0, 5) == 0  # Zero divided by non-zero
    assert division(5, 2) == 2.5  # Result is a float
    assert division(-6, -2) == 3  # Both numbers negative
    assert division(6, -2) == -3  # Positive divided by negative
    with pytest.raises(ValueError):
        division(1, 0)  # Division by zero
