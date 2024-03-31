import random

def main():
    """ 
    Call get_level to get the user-selected difficulty level.
    Use a loop to generate and present ten math problems, utilizing generate_integer for problem generation.
    For each problem, implement a mechanism to allow up to three attempts for the correct answer.
    Keep track of the number of correct answers.
    Provide immediate feedback ("EEE") for incorrect attempts.
    After three incorrect attempts, display the correct answer and move to the next problem.
    """
    pass

def get_level():
    """
    Prompt the user for a difficulty level.
    Use a loop to keep asking until a valid input (1, 2, or 3) is received.
    Return the validated level.
    """
    pass

def generate_integer(level):
    """ 
    Based on the level, generate a non-negative integer with the appropriate number of digits.
    Use the random library to generate numbers within the specified range for each level.
    Consider how to adjust the range of numbers based on the difficulty level.
    """
    pass

if __name__ == "__main__":
    main()