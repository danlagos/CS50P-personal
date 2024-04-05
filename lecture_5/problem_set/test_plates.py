from plates import is_valid

# Validation of Vanity Plate Length Constraints
def test_input_with_exact_minimum_length_and_valid_format():
    # Simulate "input with exact minimum length allowed and valid format"
    assert is_valid("AB12") is True, 'Failed to validate plate with minimum allowed length.'

def test_input_with_exact_maximum_length_and_valid_format():
    # Simulate "input with exact maximum length allowed and valid format"
    assert is_valid("AB1234") is True, 'Failed to validate plate with maximum allowed length.'

def test_input_shorter_than_minimum_length_allowed_but_otherwise_valid():
    # Simulate "input shorter than the minimum length allowed but otherwise valid"
    assert is_valid("A") is False, 'Incorrectly validated a too-short plate.'

def test_input_longer_than_maximum_length_allowed_but_otherwise_valid():
    # Simulate "input longer than the maximum length allowed but otherwise valid"
    assert is_valid("ABC12345") is False, 'Incorrectly validated a too-long plate.'

# Starts With Two Letters
def test_input_starts_with_two_letters_followed_by_valid_characters():
    # Simulate "input starts with two letters followed by valid characters"
    assert is_valid("AB123") is True, 'Failed to validate plate starting with two letters.'

def test_input_starts_with_a_digit_or_special_character():
    # Simulate "input starts with a digit or special character"
    assert is_valid("1AB234") is False, 'Incorrectly validated plate not starting with two letters.'

# Alphanumeric Only (No Special Characters or Spaces)
def test_input_contains_only_letters_and_digits_but_invalid_due_to_letter_after_number():
    # Simulate "input contains only letters and digits but is invalid due to a letter after a number sequence"
    assert is_valid("AB123C") is False, 'Incorrectly validated plate with a letter following numbers.'


def test_input_contains_special_characters_or_spaces():
    # Simulate "input contains special characters or spaces"
    assert is_valid("AB@123") is False, 'Incorrectly validated plate with special characters or spaces.'

# Number Positioning and Formatting
def test_input_with_digits_following_letters_no_leading_zeroes():
    # Simulate "input with digits following letters, no leading zeroes"
    assert is_valid("ABC123") is True, 'Failed to validate correctly formatted numbers in plate.'

def test_input_with_digits_placed_before_letters():
    # Simulate "input with digits placed before letters"
    assert is_valid("123ABC") is False, 'Incorrectly validated plate with numbers before letters.'

def test_input_with_leading_zero_in_number_portion():
    # Simulate "input with leading zero in number portion"
    assert is_valid("AB0123") is False, 'Incorrectly validated plate with leading zero in numbers.'

# Edge Cases and Special Rules (if applicable based on the problem statement details)
def test_input_with_numbers_only():
    # Simulate "input with numbers only"
    assert is_valid("123456") is False, 'Incorrectly validated numbers-only plate.'

def test_input_with_letters_only_within_allowed_length():
    # Simulate "input with letters only within allowed length"
    assert is_valid("ABCDE") is True, 'Failed to validate letters-only plate within length constraints.'

def test_input_that_includes_a_combination_of_uppercase_and_lowercase_letters():
    # Simulate "input that includes a combination of uppercase and lowercase letters"
    assert is_valid("AbCdE") is True, 'Failed to validate plate with mixed-case letters.'

# Handling Empty Strings or Unusual Inputs
def test_empty_input_string():
    # Simulate "empty input string"
    assert is_valid("") is False, 'Incorrectly validated an empty plate.'

def test_input_is_a_single_character():
    # Simulate "input is a single character"
    assert is_valid("A") is False, 'Incorrectly validated a single-character plate.'

