# logic.py
class CalculatorActions:
    @staticmethod
    def add_numbers(a, b):
        if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
            raise ValueError("Both inputs must be numeric")
        return a + b

    @staticmethod
    def subtract_numbers(a, b):
        if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
            raise ValueError("Both inputs must be numeric")
        return a - b

    @staticmethod
    def multiply_numbers(a, b):
        if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
            raise ValueError("Both inputs must be numeric")
        return a * b
