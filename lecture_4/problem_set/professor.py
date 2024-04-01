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
    level = get_level()
    correct_answers = 0
    for _ in range(10):  # Generate and solve 10 problems
        x = generate_integer(level)
        y = generate_integer(level)
        attempts = 0
        while attempts < 3:  # Allow up to 3 attempts per problem
            user_answer = input(f"{x} + {y} = ")
            try:
                if int(user_answer) == x + y:
                    correct_answers += 1
                    break  # Correct answer, move to the next problem
                else:
                    raise ValueError  # Incorrect answer, handled in the except block
            except ValueError:
                print("EEE")  # Print error message for incorrect or invalid input
                attempts += 1
                if attempts == 3:
                    print(f"{x} + {y} = {x+y}")  # Show the correct answer after 3 incorrect attempts
    print(f"Score: {correct_answers} out of 10")  # Display final score

def get_level():
    """
    Prompt the user for a difficulty level.
    Use a loop to keep asking until a valid input (1, 2, or 3) is received.
    Return the validated level.
    """
    while True:  # Loop until a valid level is received
        try:
            level = int(input("Level: "))
            if level in [1, 2, 3]:
                return level
            else:
                raise ValueError  # Not a valid level, will be caught and cause a reprompt
        except ValueError:
            # Invalid input, will cause the loop to continue and reprompt
            pass

def generate_integer(level):
    """
    Based on the level, generate a non-negative integer with the appropriate number of digits.
    Use the random library to generate numbers within the specified range for each level.
    Consider how to adjust the range of numbers based on the difficulty level.  not part of assignment.  this is extra.
    """
    # Generate and return a random single-digit integer (0-9)
    if level == 1:
        return random.randint(0, 9) 
    # Generate and return a random integer with up to two digits (0-99)
    elif level == 2:
        return random.randint(0, 99)
    # Generate and return a random integer with up to three digits (0-999)   
    elif level == 3:
        return random.randint(0, 999)
    # If the level is not 1, 2, or 3, raise a ValueError indicating an invalid level
    else:
        raise ValueError("Invalid level")

if __name__ == "__main__":
    main()