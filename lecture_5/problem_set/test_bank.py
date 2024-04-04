from bank import value
import pytest

# Tests for Specific Prefix "hello"
def test_greeting_with_hello():
    # simulate greeting with "hello", expect 0, "Greeting starting with 'hello' should return 0"
    assert value("hello") == 0

def test_greeting_with_HELLOthere():
    # simulate greeting with "HELLOthere", expect 0, "Concatenated word starting with 'HELLO' should return 0"
    assert value("HELLOthere") == 0

def test_greeting_with_hello123():
    # simulate greeting with "hello123", expect 0, "String starting with 'hello' followed by numbers should return 0"
    assert value("hello123") == 0

# Tests for Prefix "h" Not Followed by "ello"
def test_greeting_with_hi():
    # simulate greeting with "hi", expect 20, "Greeting starting with 'h' but not 'hello' should return 20"
    assert value("hi") == 20

def test_greeting_with_H():
    # simulate greeting with "H", expect 20, "Single character 'H' should return 20"
    assert value("H") == 20

def test_greeting_with_h():
    # simulate greeting with "h", expect 20, "Single character 'h' should return 20"
    assert value("h") == 20

def test_greeting_with_howdy():
    # simulate greeting with "howdy", expect 20, "Greeting starting with 'h' but not 'hello' should return 20"
    assert value("howdy") == 20

def test_greeting_with_Hi_there():
    # simulate greeting with "Hi there!", expect 20, "Greeting with 'h' and additional characters should return 20"
    assert value("Hi there!") == 20

# Tests for Greetings That Do Not Fit the Above Categories
def test_greeting_with_good_morning():
    # simulate greeting with "Good morning", expect 100, "Greeting not starting with 'h' or 'hello' should return 100"
    assert value("Good morning") == 100

def test_greeting_with_empty_string():
    # simulate greeting with "", expect 100, "Empty string should return 100"
    assert value("") == 100

def test_greeting_with_non_alphabetic_character():
    # simulate greeting with "!", expect 100, "String starting with non-alphabetic character should return 100"
    assert value("!") == 100

def test_greeting_with_numbers_followed_by_hello():
    # simulate greeting with "123hello", expect 100, "String starting with numbers followed by 'hello' should return 100"
    assert value("123hello") == 100

# Tests for Greetings With Leading Spaces or Characters
def test_greeting_with_leading_space_before_hello():
    # simulate greeting with " hello", expect 100, "String with leading space before 'hello' should return 100"
    assert value(" hello") == 100
