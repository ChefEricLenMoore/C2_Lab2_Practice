"""test_calculator.py - automated tests.

Run them with: python -m unittest -v
"""

# io.StringIO captures printed text so a test can check it.
import io
# Python's built-in testing tool - nothing extra to install.
import unittest
# redirect_stdout sends print() output into a StringIO instead of the screen.
from contextlib import redirect_stdout
# patch lets a test pretend to be the user typing answers.
from unittest.mock import patch

from calculator import add, subtract, multiply, divide
from main import ask_number, run
from utils import parse_number


class TestCalculator(unittest.TestCase):
    """Tests for the four math functions."""

    # Every method whose name starts with "test" is run as one test.
    def test_add(self):
        # assertEqual fails the test if the two values differ.
        self.assertEqual(add(2, 3), 5)
        self.assertEqual(add(-2, 3), 1)

    def test_subtract(self):
        # Order matters: 5 - 2 is 3, and 2 - 5 is -3.
        self.assertEqual(subtract(5, 2), 3)
        self.assertEqual(subtract(2, 5), -3)

    def test_multiply(self):
        self.assertEqual(multiply(6, 3), 18)
        self.assertEqual(multiply(-2, 0.5), -1.0)

    def test_divide(self):
        # / always gives a decimal.
        self.assertEqual(divide(6, 3), 2.0)
        # assertAlmostEqual allows tiny rounding differences.
        self.assertAlmostEqual(divide(1, 3), 0.3333333, places=6)

    def test_divide_by_zero_raises_value_error(self):
        # The test passes only if ValueError is raised inside this block.
        with self.assertRaises(ValueError) as caught:
            divide(6, 0)
        # Check the exact, friendly message.
        self.assertEqual(str(caught.exception), "Cannot divide by zero")


class TestParseNumber(unittest.TestCase):
    """Tests for turning typed text into a number."""

    def test_valid_numbers(self):
        self.assertEqual(parse_number("6"), 6.0)
        self.assertEqual(parse_number("-2.5"), -2.5)
        # Extra spaces are removed.
        self.assertEqual(parse_number("  3  "), 3.0)

    def test_text_is_rejected(self):
        for text in ["abc", "", "6 3"]:
            # subTest reports exactly which example failed, if one does.
            with self.subTest(text=text):
                with self.assertRaises(ValueError):
                    parse_number(text)

    def test_infinite_and_nan_are_rejected(self):
        # 1e999 is too big for a float and becomes inf.
        for text in ["inf", "-inf", "nan", "1e999"]:
            with self.subTest(text=text):
                with self.assertRaises(ValueError):
                    parse_number(text)


class TestAskNumber(unittest.TestCase):
    """Tests that bad input is asked again instead of crashing."""

    def test_asks_again_after_bad_input(self):
        # Each input() call returns the next answer: two bad, then a good one.
        with patch("builtins.input", side_effect=["abc", "inf", "6"]):
            with redirect_stdout(io.StringIO()) as output:
                result = ask_number("First number: ")
        # The first valid answer is returned...
        self.assertEqual(result, 6.0)
        # ...after one friendly message per bad answer.
        self.assertEqual(
            output.getvalue().count("Please enter a number"), 2)


class TestQuitting(unittest.TestCase):
    """Tests that quitting at a prompt says goodbye instead of crashing."""

    def test_quit_says_goodbye(self):
        # Ctrl+C raises KeyboardInterrupt; Ctrl+Z / Ctrl+D raise EOFError.
        for error in [KeyboardInterrupt, EOFError]:
            with self.subTest(error=error.__name__):
                # The first input() call acts as if the user quit.
                with patch("builtins.input", side_effect=error):
                    with redirect_stdout(io.StringIO()) as output:
                        # Must not raise an error.
                        run()
                self.assertIn("Goodbye!", output.getvalue())


# True only when you run this file directly.
if __name__ == "__main__":
    unittest.main()
