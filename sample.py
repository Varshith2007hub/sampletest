import math

class Calculator:
    def add(self, a, b):
        """Return the sum of a and b"""
        return a + b

    def divide(self, a, b):
        """Return a divided by b, raise ValueError if b is zero"""
        if b == 0:
            raise ValueError("Cannot divide by zero")
        return a / b

    def factorial(self, n):
        """Return factorial of n, raise ValueError if n is negative"""
        if n < 0:
            raise ValueError("Negative values are not allowed")
        return math.factorial(n)

def square(x):
    """Return the square of x"""
    return x * x

def is_even(n):
    """Return True if n is even, False otherwise"""
    return n % 2 == 0

# Sample usage
if __name__ == "__main__":
    calc = Calculator()
    print("Add:", calc.add(5, 3))
    print("Divide:", calc.divide(10, 2))
    print("Factorial:", calc.factorial(4))
    
    print("Square:", square(6))
    print("Is Even:", is_even(10))