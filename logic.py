class CalculatorActions:
    @staticmethod
    def add_numbers(a, b):
        if isinstance(a, bool) or isinstance(b, bool):
            raise ValueError("Inputs must not be boolean.")
        if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
            raise ValueError("Inputs must be numbers.")
        return a + b

    @staticmethod
    def subtract_numbers(a, b):
        if isinstance(a, bool) or isinstance(b, bool):
            raise ValueError("Inputs must not be boolean.")
        if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
            raise ValueError("Inputs must be numbers.")
        return a - b

    @staticmethod
    def multiply_numbers(a, b):
        if isinstance(a, bool) or isinstance(b, bool):
            raise ValueError("Inputs must not be boolean.")
        if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
            raise ValueError("Inputs must be numbers.")
        return a * b
