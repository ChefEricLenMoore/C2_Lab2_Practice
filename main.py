"""main.py - the starting point of the program. Run it with: python main.py"""  # Says how to run it.

from calculator import add, subtract, multiply, divide  # Brings in the four math functions.
from utils import parse_number  # Brings in the helper that turns text into a number.


def main():  # Groups the program's steps into one function.
    """Ask for two numbers and print every calculation."""  # Describes what main() does.
    a = parse_number(input("First number: "))  # input() reads what the user types; parse_number makes it a number.
    b = parse_number(input("Second number: "))  # Same for the second number.
    print("Add:", add(a, b))  # Prints the label and the result side by side.
    print("Subtract:", subtract(a, b))  # Prints a - b.
    print("Multiply:", multiply(a, b))  # Prints a * b.
    try:  # "try" lets us catch an error instead of crashing.
        print("Divide:", divide(a, b))  # Prints a / b when b is not 0.
    except ValueError as error:  # Runs only if divide() raised ValueError (b was 0).
        print("Divide:", error)  # Prints the friendly message "Cannot divide by zero".


if __name__ == "__main__":  # True only when you run this file directly, not when another file imports it.
    main()  # Starts the program.
