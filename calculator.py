"""calculator.py - basic math functions for the C2_Lab2_Practice lab.

Each function takes two numbers and returns the result.
"""


# "def" creates a function named add that takes two inputs, a and b.
def add(a, b):
    """Return the sum of a and b."""
    # "return" sends the answer back to whoever called the function.
    return a + b


# Order matters: subtract(5, 2) is 3, not -3.
def subtract(a, b):
    """Return a minus b."""
    return a - b


# In Python, * means multiply.
def multiply(a, b):
    """Return a times b."""
    return a * b


def divide(a, b):
    """Return a divided by b. Raises ValueError if b is 0."""
    # Check for dividing by zero BEFORE doing the math.
    if b == 0:
        # Stop with a clear, readable error message.
        raise ValueError("Cannot divide by zero")
    # Safe to divide now; / always gives a decimal (6 / 3 is 2.0).
    return a / b
