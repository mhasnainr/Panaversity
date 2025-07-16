from typing import Union

Number = Union[int, float]

class Calculator:
    """A simple calculator class with basic arithmetic operations."""

    def add(self, a: Number, b: Number) -> Number:
        return a + b

    def subtract(self, a: Number, b: Number) -> Number:
        return a - b

    def multiply(self, a: Number, b: Number) -> Number:
        return a * b

    def divide(self, a: Number, b: Number) -> float:
        if b == 0:
            raise ValueError("Cannot divide by zero.")
        return a / b

    def power(self, a: Number, b: Number) -> Number:
        return a ** b

    def modulus(self, a: Number, b: Number) -> Number:
        return a % b

def my_cal():
    """Demonstrate calculator usage with various operations."""
    calc = Calculator()
    
    print("=== Calculator Demo ===")
    print(f"Addition: 5 + 3 = {calc.add(5, 3)}")
    print(f"Subtraction: 10 - 4 = {calc.subtract(10, 4)}")
    print(f"Multiplication: 6 * 7 = {calc.multiply(6, 7)}")
    print(f"Division: 15 / 3 = {calc.divide(15, 3)}")
    print(f"Power: 2^8 = {calc.power(2, 8)}")
    print(f"Modulus: 17 % 5 = {calc.modulus(17, 5)}")
    print("=== Demo Complete ===")

def run_calculator_tests():
    calc = Calculator()

    # Addition
    assert calc.add(2, 3) == 5
    assert calc.add(2.5, 3.5) == 6.0

    # Subtraction
    assert calc.subtract(5, 3) == 2
    assert calc.subtract(5.5, 2.5) == 3.0

    # Multiplication
    assert calc.multiply(4, 3) == 12
    assert calc.multiply(2.5, 2) == 5.0

    # Division
    assert calc.divide(10, 2) == 5.0
    assert calc.divide(7, 2) == 3.5

    # Power
    assert calc.power(2, 3) == 8
    assert calc.power(9, 0.5) == 3.0

    # Modulus
    assert calc.modulus(10, 3) == 1
    assert calc.modulus(10.5, 2) == 0.5

    # Division by zero should raise an error
    try:
        calc.divide(5, 0)
        assert False, "Expected ValueError for division by zero"
    except ValueError:
        pass  # Expected

    print("All Calculator tests passed!")

if __name__ == "__main__":
    run_calculator_tests()