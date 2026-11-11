"""main.py - the starting point of the program. Run it with: python main.py"""  # Says how to run it.

from calculator import add, subtract, multiply, divide  # Brings in the four math functions.
from utils import parse_number  # Brings in the helper that turns text into a number.


def ask_number(prompt):  # Keeps asking until the user types a valid number.
    """Ask for a number and repeat the question until the answer is valid."""  # Describes what ask_number() does.
    while True:  # Loops until a valid number is typed; the "return" below is the only way out.
        try:  # "try" lets us catch bad input instead of crashing.
            return parse_number(input(prompt))  # input() reads what the user types; a valid number is sent back.
        except ValueError:  # parse_number() raised ValueError: not a number (like "abc"), or inf/nan.
            print("Please enter a number, for example 6 or 2.5.")  # Explains what to type; the loop then asks again.


def main():  # Groups the program's steps into one function.
    """Ask for two numbers and print every calculation."""  # Describes what main() does.
    a = ask_number("First number: ")  # Asks for the first number, repeating until it is valid.
    b = ask_number("Second number: ")  # Same for the second number.
    print("Add:", add(a, b))  # Prints the label and the result side by side.
    print("Subtract:", subtract(a, b))  # Prints a - b.
    print("Multiply:", multiply(a, b))  # Prints a * b.
    try:  # "try" lets us catch an error instead of crashing.
        print("Divide:", divide(a, b))  # Prints a / b when b is not 0.
    except ValueError as error:  # Runs only if divide() raised ValueError (b was 0).
        print("Divide:", error)  # Prints the friendly message "Cannot divide by zero".


if __name__ == "__main__":  # True only when you run this file directly, not when another file imports it.
    main()  # Starts the program.
