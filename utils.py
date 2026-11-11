"""utils.py - helper functions used by main.py."""  # Describes the file's purpose.

import math  # Gives us math.isfinite(), which spots "inf" and "nan".


def parse_number(text):  # Turns text such as "3.5" into a number Python can do math with.
    """Convert text to a float. Raises ValueError if it is not a normal, finite number."""  # Documents the behavior.
    number = float(text.strip())  # .strip() removes extra spaces; float() turns "3.5" into 3.5, or raises ValueError for "abc".
    if not math.isfinite(number):  # "inf", "-inf" and "nan" are valid floats in Python, but meaningless for a calculator.
        raise ValueError(f"{text.strip()!r} is not a finite number")  # Treats them like any other bad input.
    return number  # Sends back the checked number.
