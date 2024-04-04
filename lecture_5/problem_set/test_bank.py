from bank import value
import pytest

"""
Tests for Specific Prefix "hello"
•	simulate greeting with "hello", expect 0, "Greeting starting with 'hello' should return 0"
•	simulate greeting with "HELLOthere", expect 0, "Concatenated word starting with 'HELLO' should return 0"
•	simulate greeting with "hello123", expect 0, "String starting with 'hello' followed by numbers should return 0"

Tests for Prefix "h" Not Followed by "ello"
•	simulate greeting with "hi", expect 20, "Greeting starting with 'h' but not 'hello' should return 20"
•	simulate greeting with "H", expect 20, "Single character 'H' should return 20"
•	simulate greeting with "h", expect 20, "Single character 'h' should return 20"
•	simulate greeting with "howdy", expect 20, "Greeting starting with 'h' but not 'hello' should return 20"
•	simulate greeting with "Hi there!", expect 20, "Greeting with 'h' and additional characters should return 20"

Tests for Greetings That Do Not Fit the Above Categories
•	simulate greeting with "Good morning", expect 100, "Greeting not starting with 'h' or 'hello' should return 100"
•	simulate greeting with "", expect 100, "Empty string should return 100"
•	simulate greeting with "!", expect 100, "String starting with non-alphabetic character should return 100"
•	simulate greeting with "123hello", expect 100, "String starting with numbers followed by 'hello' should return 100"

Tests for Greetings With Leading Spaces or Characters
•	simulate greeting with " hello", expect 100, "String with leading space before 'hello' should return 100"

"""