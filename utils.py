"""utils.py - helper functions used by main.py."""

# math.isfinite() spots "inf" and "nan".
import math


def parse_number(text):
    """Convert text such as "3.5" to a float.

    Raises ValueError if the text is not a normal, finite number.
    """
    # .strip() removes extra spaces; float() turns "3.5" into 3.5,
    # or raises ValueError for text like "abc".
    number = float(text.strip())
    # "inf", "-inf" and "nan" are valid floats in Python,
    # but meaningless for a calculator, so treat them as bad input.
    if not math.isfinite(number):
        raise ValueError(f"{text.strip()!r} is not a finite number")
    return number
