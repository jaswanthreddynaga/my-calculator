# My Command-Line Calculator

A simple yet robust command-line calculator built in Python with a focus on clean code, comprehensive testing, and continuous integration.

## Features

- **REPL Interface:** Continuous interaction for performing multiple calculations.
- **Arithmetic Operations:** Supports addition, subtraction, multiplication, and division.
- **Input Validation:** Gracefully handles invalid number and operation inputs.
- **Error Handling:** Catches and provides a meaningful message for division by zero errors.

## Project Structure

my-calculator/

├── calculator/
│   ├── operations.py
│   └── main.py

├── tests/
│   └── test_operations.py

├── .github/
│   └── workflows/
│       └── test.yml

├── README.md

├── requirements.txt

└── .gitignore

## Setup & Usage

### 1. Clone the repository

```bash
git clone [https://github.com/your-username/my-calculator.git](https://github.com/your-username/my-calculator.git)
cd my-calculator
```
### 2. Create and activate a virtual environment

```Bash
python -m venv venv
source venv/bin/activate
```
### 3. Install dependencies

```Bash
pip install -r requirements.txt
```
### 4. Run the calculator

```Bash
python calculator/main.py
```
### 5. Running Tests

To run the unit tests and check for 100% test coverage:

```Bash
pytest --cov=calculator
```
The GitHub Actions workflow is configured to automatically run these tests on every push and pull request, ensuring all changes maintain a 100% test coverage threshold.

### Author
Jaswanth Reddy Naga
