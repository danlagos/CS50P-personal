from fuel import convert, gauge

"""

Tests for convert function:

Handling Non-Integer Input
simulate "input of 'three/four'" expect "to raise ValueError" failure message "Expected ValueError for non-integer values"

Numerator Greater Than Denominator
simulate "input of '5/4'" expect "to raise ValueError" failure message "Expected ValueError when numerator is greater than denominator"

Zero Denominator
simulate "input of '1/0'" expect "to raise ZeroDivisionError" failure message "Expected ZeroDivisionError for zero denominator"

Valid Input Conversion
simulate "input of '50/100'" expect "to return 50" failure message "Expected 50% when input is 50/100"

Negative Number Handling
simulate "input of '-1/10'" expect "to raise ValueError" failure message "Expected ValueError for negative numbers"

Tests for gauge function:

Low Boundary Condition for 'E'
simulate "input of 1" expect "to return 'E'" failure message "Expected 'E' for input of 1"

High Boundary Condition for 'F'
simulate "input of 99" expect "to return 'F'" failure message "Expected 'F' for input of 99"

Percentage Display for Normal Range
simulate "input of 25" expect "to return '25%'" failure message "Expected '25%' for input of 25"

Edge Case for Low Percentage
simulate "input of 0" expect "to return 'E'" failure message "Expected 'E' for input of 0"

Edge Case for High Percentage
simulate "input of 100" expect "to return 'F'" failure message "Expected 'F' for input of 100"

"""
def test_convert_non_integer_input():
    # simulate "input of 'three/four'" expect "to raise ValueError" failure message "Expected ValueError for non-integer values"
    with pytest.raises(ValueError, match="Expected ValueError for non-integer values"):
        convert("three/four")

def test_convert_numerator_greater_than_denominator():
    # simulate "input of '5/4'" expect "to raise ValueError" failure message "Expected ValueError when numerator is greater than denominator"
    with pytest.raises(ValueError, match="Expected ValueError when numerator is greater than denominator"):
        convert("5/4")

def test_convert_zero_denominator():
    # simulate "input of '1/0'" expect "to raise ZeroDivisionError" failure message "Expected ZeroDivisionError for zero denominator"
    with pytest.raises(ZeroDivisionError, match="Expected ZeroDivisionError for zero denominator"):
        convert("1/0")

def test_convert_valid_input():
    # simulate "input of '50/100'" expect "to return 50" failure message "Expected 50% when input is 50/100"
    assert convert("50/100") == 50, "Expected 50% when input is 50/100"

def test_convert_negative_numbers():
    # simulate "input of '-1/10'" expect "to raise ValueError" failure message "Expected ValueError for negative numbers"
    with pytest.raises(ValueError, match="Expected ValueError for negative numbers"):
        convert("-1/10")

