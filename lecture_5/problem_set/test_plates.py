from plates import is_valid

def test_cs50_valid():
    assert is_valid("CS50") == True, "CS50 should be considered a valid plate"

def test_cs05_invalid():
    assert is_valid("CS05") == False, "CS05 should be invalid because the first digit cannot be '0'"

def test_cs50p_invalid():
    assert is_valid("CS50P") == False, "CS50P should be invalid because numbers must come at the end only"

def test_pi3_14_invalid():
    assert is_valid("PI3.14") == False, "PI3.14 should be invalid because it contains a period"

def test_h_invalid():
    assert is_valid("H") == False, "H should be invalid because it is below the minimum character requirement of 2"

def test_outatime_invalid():
    assert is_valid("OUTATIME") == False, "OUTATIME should be invalid because it exceeds the maximum character limit of 6"

# new test cases

""" 

def test_valid_string():
    assert is_valid("AB1234") == True, "AB1234 should be valid"

def test_only_letters():
    assert is_valid("AB") == False, "AB should be invalid because it doesn't contain any numbers"

def test_only_numbers():
    assert is_valid("1234") == False, "1234 should be invalid because it doesn't contain any letters"

def test_contains_punctuation():
    assert is_valid("AB.1234") == False, "AB.1234 should be invalid because it contains a period"

def test_contains_punctuation_at_end():
    assert is_valid("AB1234.") == False, "AB1234. should be invalid because it contains a period at the end"

def test_contains_dash():
    assert is_valid("AB-1234") == False, "AB-1234 should be invalid because it contains a dash"

def test_first_number_zero():
    assert is_valid("AB0123") == False, "AB0123 should be invalid because the first number is '0'"

def test_starts_with_one_letter():
    assert is_valid("A1234") == False, "A1234 should be invalid because it starts with only one letter"

def test_more_than_six_characters():
    assert is_valid("AB12345") == False, "AB12345 should be invalid because it has more than 6 characters"
"""