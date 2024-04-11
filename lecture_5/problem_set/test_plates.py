import pytest
from plates import is_valid  # Make sure this import works based on your project structure.

def test_cs50_valid():
    assert is_valid("CS50") is True, "CS50 should be considered a valid plate"

def test_cs05_invalid():
    assert is_valid("CS05") is False, "CS05 should be invalid because the first digit cannot be '0'"

def test_cs50p_invalid():
    assert is_valid("CS50P") is False, "CS50P should be invalid because numbers must come at the end only"

def test_pi3_14_invalid():
    assert is_valid("PI3.14") is False, "PI3.14 should be invalid because it contains a period"

def test_h_invalid():
    assert is_valid("H") is False, "H should be invalid because it is below the minimum character requirement of 2"

def test_outatime_invalid():
    assert is_valid("OUTATIME") is False, "OUTATIME should be invalid because it exceeds the maximum character limit of 6"
