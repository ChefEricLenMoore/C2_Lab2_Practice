"""calculator.py - basic math functions for the C2_Lab2_Practice lab.

Each function takes two numbers and returns the result.
"""  # A docstring at the top describes what the whole file is for.


def add(a, b):  # "def" creates a function named add that takes two inputs, a and b.
    """Return the sum of a and b."""  # A one-line docstring says what the function does.
    return a + b  # "return" sends the answer back to whoever called the function.


def subtract(a, b):  # Defines subtract with the same two inputs.
    """Return a minus b."""  # Order matters: subtract(5, 2) is 3, not -3.
    return a - b  # Sends back the difference.
