"""test_calculator.py - automated tests. Run them with: python -m unittest -v"""  # Says what the file is and how to run it.

import io  # io.StringIO captures printed text so a test can check it.
import unittest  # Python's built-in testing tool - nothing extra to install.
from contextlib import redirect_stdout  # Sends print() output into a StringIO instead of the screen.
from unittest.mock import patch  # Lets a test pretend to be the user typing answers.

from calculator import add, subtract, multiply, divide  # The four math functions under test.
from main import ask_number  # The prompt helper that should re-ask on bad input.
from utils import parse_number  # The text-to-number helper under test.


class TestCalculator(unittest.TestCase):  # A group of tests for calculator.py.
    """Tests for the four math functions."""  # Describes the group.

    def test_add(self):  # Every method whose name starts with "test" is run as one test.
        self.assertEqual(add(2, 3), 5)  # assertEqual fails the test if the two values differ.
        self.assertEqual(add(-2, 3), 1)  # Negative numbers work too.

    def test_subtract(self):  # Checks subtract().
        self.assertEqual(subtract(5, 2), 3)  # Order matters: 5 - 2 is 3...
        self.assertEqual(subtract(2, 5), -3)  # ...and 2 - 5 is -3.

    def test_multiply(self):  # Checks multiply().
        self.assertEqual(multiply(6, 3), 18)  # Whole numbers.
        self.assertEqual(multiply(-2, 0.5), -1.0)  # A negative times a decimal.

    def test_divide(self):  # Checks divide() for normal numbers.
        self.assertEqual(divide(6, 3), 2.0)  # / always gives a decimal.
        self.assertAlmostEqual(divide(1, 3), 0.3333333, places=6)  # assertAlmostEqual allows tiny rounding differences.

    def test_divide_by_zero_raises_value_error(self):  # Checks the review fix from PR #1.
        with self.assertRaises(ValueError) as caught:  # The test passes only if ValueError is raised inside this block.
            divide(6, 0)  # Dividing by zero must not crash with ZeroDivisionError.
        self.assertEqual(str(caught.exception), "Cannot divide by zero")  # Checks the exact, friendly message.


class TestParseNumber(unittest.TestCase):  # A group of tests for utils.py.
    """Tests for turning typed text into a number."""  # Describes the group.

    def test_valid_numbers(self):  # Normal input.
        self.assertEqual(parse_number("6"), 6.0)  # Whole number.
        self.assertEqual(parse_number("-2.5"), -2.5)  # Negative decimal.
        self.assertEqual(parse_number("  3  "), 3.0)  # Extra spaces are removed.

    def test_text_is_rejected(self):  # Input that is not a number at all.
        for text in ["abc", "", "6 3"]:  # Several bad examples, tested one after another.
            with self.subTest(text=text):  # subTest reports exactly which example failed, if one does.
                with self.assertRaises(ValueError):  # Each one must raise ValueError.
                    parse_number(text)  # Tries to convert the bad text.

    def test_infinite_and_nan_are_rejected(self):  # Valid floats that make no sense for a calculator.
        for text in ["inf", "-inf", "nan", "1e999"]:  # 1e999 is too big and becomes inf.
            with self.subTest(text=text):  # Reports which example failed, if one does.
                with self.assertRaises(ValueError):  # Each one must raise ValueError.
                    parse_number(text)  # Tries to convert it.


class TestAskNumber(unittest.TestCase):  # Tests for the prompt helper in main.py.
    """Tests that bad input is asked again instead of crashing."""  # Describes the group.

    def test_asks_again_after_bad_input(self):  # Simulates a user who types two bad answers, then a good one.
        with patch("builtins.input", side_effect=["abc", "inf", "6"]):  # Each input() call returns the next answer.
            with redirect_stdout(io.StringIO()) as output:  # Captures what the program prints.
                result = ask_number("First number: ")  # Runs the helper with the fake answers.
        self.assertEqual(result, 6.0)  # The first valid answer is returned.
        self.assertEqual(output.getvalue().count("Please enter a number"), 2)  # One friendly message per bad answer.


if __name__ == "__main__":  # True only when you run this file directly.
    unittest.main()  # Runs every test above.
