import random

def main():
    # Prompt the user to enter a game level as a positive integer.
    level = get_validated_input("Level: ")
    
    # Generate a target number within the range of 1 to the chosen level.
    target_number = generate_random_number(level)
    
    # Initiate the guessing game, where the user tries to guess the target number.
    run_guessing_game(target_number)

def get_validated_input(prompt):
    """
    Repeatedly prompt the user until a valid positive integer is entered.
    This function is used for both getting the game level and the user's guesses.
    It ensures that the input is not only an integer but also a positive one.
    Returns the validated integer.
    """
    while True:
        user_input = input(prompt)  # Request input from the user.
        try:
            # Convert the input from a string to an integer.
            user_input_as_int = int(user_input)
            # Check if the integer is positive; if not, reprompt the user.
            if user_input_as_int > 0:
                return user_input_as_int
            else:
                print("Please enter a positive integer.")
        except ValueError:
            # If the input cannot be converted to an integer, notify the user and reprompt.
            print("Invalid input. Please enter a positive integer.")

def generate_random_number(max_value):
    """
    Generates a random integer within the inclusive range between 1 and the provided max_value.
    This random number serves as the target for the user to guess.
    """
    return random.randint(1, max_value)
    
def run_guessing_game(target):
    """
    Conducts the guessing game by prompting the user to guess the randomly generated target number.
    It provides feedback on each guess - indicating if it's too high, too low, or correct.
    The game continues until the user correctly guesses the target number.
    """
    while True:
        # Request a guess from the user, ensuring it is a positive integer.
        user_guess = get_validated_input("Guess: ")
        # Compare the guess to the target number and provide appropriate feedback.
        if user_guess < target:
            print("Too small!")
        elif user_guess > target:
            print("Too large!")
        else:
            # When the guess is correct, congratulate the user and exit the loop.
            print("Just right!")
            break
        
if __name__ == "__main__":
    main()
