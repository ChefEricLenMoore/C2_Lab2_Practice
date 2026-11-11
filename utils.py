"""utils.py - helper functions used by main.py."""  # Describes the file's purpose.


def parse_number(text):  # Turns text such as "3.5" into a number Python can do math with.
    """Convert text to a float. Raises ValueError if the text is not a number."""  # Documents the behavior.
    return float(text.strip())  # .strip() removes extra spaces; float() converts "3.5" to 3.5.
