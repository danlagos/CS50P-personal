import pytest
from datetime import datetime
from seasons import calculate_date, format_minutes_as_words

def test_specific_birthdate():
    """
    Test that calculate_date correctly calculates the minutes from a known past date to today.
    Example with a fixed date.
    """
    birthdate = '1990-01-01'
    birthdate_date = datetime.strptime(birthdate, '%Y-%m-%d').date()
    today = datetime.now().date()
    expected_days = (today - birthdate_date).days
    expected_minutes = expected_days * 1440
    
    assert calculate_date(birthdate) == expected_minutes, f"Expected {expected_minutes} minutes, got {calculate_date(birthdate)}"

def test_invalid_date_format():
    """
    Test that calculate_date raises ValueError for non-existent dates.
    """
    invalid_date = "1990-02-30"
    with pytest.raises(ValueError):
        calculate_date(invalid_date)

def test_invalid_input_type():
    """
    Test that calculate_date raises ValueError for non-string inputs.
    """
    invalid_input = 123456  # Non-string input
    with pytest.raises(TypeError):
        calculate_date(invalid_input)


# Unit tests for format_minutes_as_words()
def test_format_small_number():
    """
    Test that small numbers are formatted correctly into words.
    """
    assert format_minutes_as_words(120) == "One hundred twenty minutes", "Failed to format small numbers"

def test_format_large_number():
    """
    Test that large numbers are formatted correctly into words.
    """
    assert format_minutes_as_words(525600) == "Five hundred twenty-five thousand, six hundred minutes", "Failed to format large numbers"

def test_format_zero():
    """
    Test that zero is formatted correctly into words.
    """
    assert format_minutes_as_words(0) == "Zero minutes", "Failed to format zero"

def test_format_negative_number():
    """
    Test that negative numbers are handled appropriately.
    """
    assert format_minutes_as_words(-150) == "Minus one hundred fifty minutes", "Failed to format negative numbers"

def test_format_very_large_number():
    """
    Test formatting of very large numbers.
    """
    assert format_minutes_as_words(1000000) == "One million minutes", "Failed to format very large numbers"
