import pytest
from logic import CalculatorActions


def test_add_numbers():
    assert CalculatorActions.add_numbers(1, 2) == 3
    assert CalculatorActions.add_numbers(-1, 1) == 0
    assert CalculatorActions.add_numbers(-1, -1) == -2
    assert CalculatorActions.add_numbers(0, 0) == 0


def test_subtract_numbers():
    assert CalculatorActions.subtract_numbers(10, 5) == 5
    assert CalculatorActions.subtract_numbers(0, 0) == 0
    assert CalculatorActions.subtract_numbers(-1, -1) == 0
    assert CalculatorActions.subtract_numbers(-1, 1) == -2


def test_multiply_numbers():
    assert CalculatorActions.multiply_numbers(3, 4) == 12
    assert CalculatorActions.multiply_numbers(-1, 1) == -1
    assert CalculatorActions.multiply_numbers(0, 5) == 0
    assert CalculatorActions.multiply_numbers(-2, -3) == 6


def test_multiply_numbers_invalid_input():
    # Test with string inputs
    with pytest.raises(ValueError):
        CalculatorActions.multiply_numbers('a', 1)
    with pytest.raises(ValueError):
        CalculatorActions.multiply_numbers(1, 'b')
    with pytest.raises(ValueError):
        CalculatorActions.multiply_numbers('a', 'b')

    # Test with None inputs
    with pytest.raises(ValueError):
        CalculatorActions.multiply_numbers(None, 3)
    with pytest.raises(ValueError):
        CalculatorActions.multiply_numbers(3, None)

    # Test with boolean inputs
    with pytest.raises(ValueError):
        CalculatorActions.multiply_numbers(True, 3)
    with pytest.raises(ValueError):
        CalculatorActions.multiply_numbers(3, False)
