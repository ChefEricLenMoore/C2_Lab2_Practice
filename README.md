# C2_Lab2_Practice

A small Python calculator built as practice for **Course 2, Lab 2: Using AI with GitHub (Web Interface)**.
The repository is used to practise Pull Requests, commit messages, README updates and code review with AI help.

## Features

- Add, subtract, multiply and divide two numbers
- Clear error message when dividing by zero (`Divide: Cannot divide by zero`) instead of a crash
- Asks again if you type something that isn't a number (like `abc`, `inf` or `nan`)
- Says "Goodbye!" if you quit at a prompt with Ctrl+C (or Ctrl+Z then Enter on Windows) instead of showing an error
- Simple command-line prompt (`main.py`)
- Automated tests (`test_calculator.py`)

## Project structure

| File | Purpose |
|------|---------|
| `main.py` | Starting point. Asks for two numbers and prints the results. |
| `calculator.py` | The four math functions. |
| `utils.py` | Helper that turns typed text into a number and rejects bad input. |
| `test_calculator.py` | Automated tests for the math functions and input handling. |
| `README.md` | This file. |
| `.gitignore` | Tells Git which files not to track (caches, virtual environments, editor files). |
| `LICENSE` | The MIT License – how others may use this code. |
| `docs/evidence/` | Screenshots showing the Lab 2 tasks were completed, grouped by task ([details](docs/evidence/README.md)). |

## Requirements

- Python 3 ([download](https://www.python.org/downloads/)) – tested with Python 3.13
- No extra packages are needed

## Setup

```bash
git clone https://github.com/ChefEricLenMoore/C2_Lab2_Practice.git
cd C2_Lab2_Practice
```

## Run it

```bash
python main.py
```

Example:

```
First number: 6
Second number: 3
Add: 9.0
Subtract: 3.0
Multiply: 18.0
Divide: 2.0
```

Results are shown as decimals (for example `9.0`) because the inputs are read as decimal numbers.

If you type something that isn't a number, the program asks again:

```
First number: abc
Please enter a number, for example 6 or 2.5.
First number: 6
```

## Run it online (nothing to install)

[![Open in GitHub Codespaces](https://github.com/codespaces/badge.svg)](https://codespaces.new/ChefEricLenMoore/C2_Lab2_Practice?quickstart=1)

1. Click the button above (or go to
   <https://codespaces.new/ChefEricLenMoore/C2_Lab2_Practice?quickstart=1>)
   and sign in to GitHub.
2. Click **Create codespace**. A copy of VS Code opens in your browser with
   Python already installed.
3. In the **Terminal** at the bottom, run `python main.py` to use the
   calculator, or `python -m unittest -v` to run the tests.

Personal GitHub accounts get free Codespaces hours each month. Stop or delete
the codespace when you are done (**github.com/codespaces**).

## Run the tests

```bash
python -m unittest -v
```

This runs the 10 tests in `test_calculator.py` using Python's built-in `unittest` – nothing extra to install.

## Use the functions in your own code

```python
from calculator import add, divide

print(add(2, 3))      # 5
print(divide(6, 3))   # 2.0
```

## Lab tasks covered

1. AI review of a Pull Request
2. AI summary of the PR's changes
3. AI rewrite of a weak commit message
4. AI explanation of an unfamiliar repository
5. AI improvement of this README
6. AI-drafted reply to a review comment

## License

This project is licensed under the [MIT License](LICENSE).
