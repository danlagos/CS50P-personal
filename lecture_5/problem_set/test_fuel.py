import pytest
from fuel import convert, gauge

# tests for convert function
def test_convert_non_integer_input():
    # simulate "input of 'three/four'" expect "to raise ValueError" failure message "Expected ValueError for non-integer values"
    with pytest.raises(ValueError, match="Please enter both numerator and denominator as integers."):
        convert("three/four")

def test_convert_numerator_greater_than_denominator():
    # simulate "input of '5/4'" expect "to raise ValueError" failure message "Expected ValueError when numerator is greater than denominator"
    with pytest.raises(ValueError, match="Numerator must not be larger than denominator."):
        convert("5/4")

def test_convert_zero_denominator():
    # simulate "input of '1/0'" expect "to raise ZeroDivisionError" failure message "Expected ZeroDivisionError for zero denominator"
    with pytest.raises(ZeroDivisionError, match="Denominator cannot be zero."):
        convert("1/0")

def test_convert_valid_input():
    # simulate "input of '50/100'" expect "to return 50" failure message "Expected 50% when input is 50/100"
    assert convert("50/100") == 50, "Expected 50% when input is 50/100"

def test_convert_negative_numbers():
    # simulate "input of '-1/10'" expect "to raise ValueError" failure message "Expected ValueError for negative numbers"
    with pytest.raises(ValueError, match="Negative numbers are not allowed."):
        convert("-1/10")

#tests for gauge function
def test_gauge_low_boundary():
    # simulate "input of 1" expect "to return 'E'" failure message "Expected 'E' for input of 1"
    assert gauge(1) == "E", "Expected 'E' for input of 1"

def test_gauge_high_boundary():
    # simulate "input of 99" expect "to return 'F'" failure message "Expected 'F' for input of 99"
    assert gauge(99) == "F", "Expected 'F' for input of 99"

def test_gauge_normal_percentage():
    # simulate "input of 25" expect "to return '25%'" failure message "Expected '25%' for input of 25"
    assert gauge(25) == "25%", "Expected '25%' for input of 25"

def test_gauge_zero_input():
    # simulate "input of 0" expect "to return 'E'" failure message "Expected 'E' for input of 0"
    assert gauge(0) == "E", "Expected 'E' for input of 0"

def test_gauge_one_hundred_input():
    # simulate "input of 100" expect "to return 'F'" failure message "Expected 'F' for input of 100"
    assert gauge(100) == "F", "Expected 'F' for input of 100"