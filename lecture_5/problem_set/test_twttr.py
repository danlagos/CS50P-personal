import twttr

"""
function that tests 
    - Simulate input with mixed lowercase and uppercase vowels, expect all vowels to be removed.
    - Simulate input with only lowercase vowels, expect a string with vowels removed.
    - Simulate input with only uppercase vowels, expect a string with vowels removed.
    
function that tests for edge cases
    - Simulate inputting an empty string, expect an empty string in return.
    - Simulate inputting a string with no vowels, expect the original string to be returned unchanged.
    - Simulate inputting a string composed entirely of vowels, expect an empty string in return.

function that tests for robustness
    - Simulate inputting strings with mixed characters (letters, numbers, special characters), expect only vowels to be removed, with other characters unaffected.
    - Simulate inputting strings with spaces, expect spaces to be preserved in the output.
    
Function that tests for non-string input
    - simulate inputting a list, expect an error that can be caught with try/catch block
    - simulate inputting a dict, expect an error that can be caught with try/catch block
    - simulate inputting a int, expect an error that can be caught with try/catch block
    - simulate inputting a float, expect an error that can be caught with try/catch block
    - simulate inputting a boolean, expect an error that can be caught with try/catch block
"""