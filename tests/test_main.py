from unittest.mock import patch
import pytest
from calculator.main import get_operation, get_numbers, main

# Test get_operation() to ensure it handles valid and invalid input
@pytest.mark.parametrize("input_value, expected_output", [
    ('+', '+'),
    ('-', '-'),
    ('*', '*'),
    ('/', '/'),
    ('exit', 'exit')
])
def test_get_operation_valid(input_value, expected_output):
    with patch('builtins.input', return_value=input_value):
        assert get_operation() == expected_output

def test_get_operation_invalid_then_valid():
    with patch('builtins.input', side_effect=['invalid', '+']):
        assert get_operation() == '+'

# Test get_numbers() to check for valid and invalid number inputs
def test_get_numbers_valid():
    with patch('builtins.input', side_effect=['10', '5']):
        assert get_numbers() == (10.0, 5.0)

def test_get_numbers_invalid_then_valid():
    with patch('builtins.input', side_effect=['abc', '10', '5']):
        assert get_numbers() == (10.0, 5.0)


def test_main_division_by_zero():
    # Simulate a division by zero error
    user_inputs = ['/', '10', '0', 'exit']
    with patch('builtins.input', side_effect=user_inputs), \
         patch('builtins.print') as mock_print:
        main()
        # Check if the error message was printed
        assert mock_print.call_args_list[1].args[0] == 'Error: Cannot divide by zero.\n'
