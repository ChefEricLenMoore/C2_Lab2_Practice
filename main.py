"""main.py - the starting point of the program.

Run it with: python main.py
"""

# Bring in the four math functions and the text-to-number helper.
from calculator import add, subtract, multiply, divide
from utils import parse_number


def ask_number(prompt):
    """Ask for a number and repeat the question until the answer is valid."""
    # Loop until a valid number is typed; "return" is the only way out.
    while True:
        # "try" lets us catch bad input instead of crashing.
        try:
            # input() reads what the user types; a valid number is returned.
            return parse_number(input(prompt))
        # parse_number() raised ValueError: not a number, or inf/nan.
        except ValueError:
            # Explain what to type; the loop then asks again.
            print("Please enter a number, for example 6 or 2.5.")


def main():
    """Ask for two numbers and print every calculation."""
    a = ask_number("First number: ")
    b = ask_number("Second number: ")
    # Print each label and its result side by side.
    print("Add:", add(a, b))
    print("Subtract:", subtract(a, b))
    print("Multiply:", multiply(a, b))
    try:
        print("Divide:", divide(a, b))
    # divide() raises ValueError when b is 0.
    except ValueError as error:
        # Prints the friendly message "Cannot divide by zero".
        print("Divide:", error)


def run():
    """Run main(); print "Goodbye!" instead of an error if the user quits."""
    try:
        main()
    # EOFError: Ctrl+Z then Enter (Windows) or Ctrl+D (Mac/Linux).
    # KeyboardInterrupt: Ctrl+C.
    except (EOFError, KeyboardInterrupt):
        # A friendly message on a new line instead of a Python traceback.
        print("\nGoodbye!")


# True only when you run this file directly,
# not when another file (like the tests) imports it.
if __name__ == "__main__":
    run()
