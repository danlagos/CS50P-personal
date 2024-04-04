import pytest
from twttr import shorten


def test_shorten_with_mixed_vowels():
    # Simulate input with mixed lowercase and uppercase vowels, expect all vowels to be removed.
    input_str = "MixEdVowels"
    expected_output = "MxdVwls"
    assert shorten(input_str) == expected_output, "Failed to remove both lowercase and uppercase vowels"

def test_shorten_with_only_lowercase_vowels():
    # Simulate input with only lowercase vowels, expect a string with vowels removed.
    input_str = "aeiou"
    expected_output = ""
    assert shorten(input_str) == expected_output, "Failed to remove lowercase vowels"

def test_shorten_with_only_uppercase_vowels():
    # Simulate input with only uppercase vowels, expect a string with vowels removed.
    input_str = "AEIOU"
    expected_output = ""
    assert shorten(input_str) == expected_output, "Failed to remove uppercase vowels"

def test_shorten_with_empty_string():
    # Simulate inputting an empty string, expect an empty string in return.
    input_str = ""
    expected_output = ""
    assert shorten(input_str) == expected_output, "Failed to return empty string for empty input"

def test_string_with_no_vowels():
    # Simulate inputting a string with no vowels, expect the original string to be returned unchanged.
    input_str = "bcdfg"
    expected_output = "bcdfg"
    assert shorten(input_str) == expected_output, "Failed to return original string for consonants only"

def test_string_composed_entirely_of_vowels():
    # Simulate inputting a string composed entirely of vowels, expect an empty string in return.
    input_str = "aeiouAEIOU"
    expected_output = ""
    assert shorten(input_str) == expected_output, "Failed to return empty string for vowels only"

def test_string_with_mixed_characters():
    # Simulate inputting strings with mixed characters (letters, numbers, special characters), expect only vowels to be removed, with other characters unaffected.
    input_str = "Pyth0n! Is Aw3some."
    expected_output = "Pyth0n! s w3sm."
    assert shorten(input_str) == expected_output, "Failed to correctly remove vowels from mixed character string"

def test_string_with_spaces():
    # Simulate inputting strings with spaces, expect spaces to be preserved in the output.
    input_str = "Hello World"
    expected_output = "Hll Wrld"
    assert shorten(input_str) == expected_output, "Failed to preserve spaces"

@pytest.mark.parametrize("test_input", [[], {}, 42, 3.14, True])
def test_non_string_input(test_input):
    # Simulate inputting non-string types, expect an error.
    with pytest.raises(TypeError):
        shorten(test_input)
