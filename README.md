# C2_Lab2_Practice

A small Python calculator built as practice for **Course 2, Lab 2: Using AI with GitHub (Web Interface)**.
The repository is used to practise Pull Requests, commit messages, README updates and code review with AI help.

> **Status:** the calculator code is in [Pull Request #1](https://github.com/ChefEricLenMoore/C2_Lab2_Practice/pull/1)
> (branch `features`). It will appear on `main` once that PR is merged.

## Features

- Add, subtract, multiply and divide two numbers
- Simple command-line prompt (`main.py`)

**Known limitation:** dividing by zero currently crashes the program. A fix is planned before PR #1 is merged.

## Project structure

| File | Purpose |
|------|---------|
| `main.py` | Starting point. Asks for two numbers and prints the results. |
| `calculator.py` | The four math functions. |
| `utils.py` | Helper that turns typed text into a number. |
| `README.md` | This file. |
| `.gitignore` | Tells Git which files not to track (caches, virtual environments, editor files). |

## Requirements

- Python 3 ([download](https://www.python.org/downloads/)) – tested with Python 3.13
- No extra packages are needed

## Setup

```bash
git clone https://github.com/ChefEricLenMoore/C2_Lab2_Practice.git
cd C2_Lab2_Practice
git switch features   # until PR #1 is merged, the code lives on this branch
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
