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

# test_main.py (addition)


# New tests that check for the presence of a specific print call

def test_main_multiplication_then_exit():
    # Simulate a user performing multiplication and then exiting
    user_inputs = ['*', '5', '3', 'exit']
    with patch('builtins.input', side_effect=user_inputs), \
         patch('builtins.print') as mock_print:
        main()
        # Assert that the correct result was printed
        mock_print.assert_any_call('Result: 15.0\n')

def test_main_division_then_exit():
    # Simulate a user performing division and then exiting
    user_inputs = ['/', '10', '2', 'exit']
    with patch('builtins.input', side_effect=user_inputs), \
         patch('builtins.print') as mock_print:
        main()
        # Assert that the correct result was printed
        mock_print.assert_any_call('Result: 5.0\n')
             
def test_main_division_by_zero():
    # Simulate a division by zero and then exit
    user_inputs = ['/', '10', '0', 'exit']
    with patch('builtins.input', side_effect=user_inputs), \
         patch('builtins.print') as mock_print:
        main()
        # The error print is at call_args_list[4] for this sequence
        assert mock_print.call_args_list[4].args[0] == 'Error: Cannot divide by zero.\n'
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
