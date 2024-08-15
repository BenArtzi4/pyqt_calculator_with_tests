# test_logic_pytest.py
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
