import random

def main():
    # Prompt the user for a level, ensuring it's a positive integer, then start the guessing game.
    level = get_validated_input("Level: ")
    target_number = generate_random_number(level)
    run_guessing_game(target_number)

def get_validated_input(prompt):
    """
    Repeatedly prompt the user with the given prompt until a valid positive integer is entered.
    This function ensures that input is a positive integer, suitable for both getting the game level
    and the user's guesses. Invalid or non-positive inputs result in reprompting.
    """
    while True:
        user_input = input(prompt)  # Request input from the user as a string.
        try:
            user_input_as_int = int(user_input)  # Attempt to convert the input to an integer.
            if user_input_as_int > 0:
                return user_input_as_int  # Return the integer if it's positive.
            # If the input is not positive, the loop continues, implicitly reprompting the user.
        except ValueError:
            # If the input cannot be converted to an integer, the loop continues, implicitly reprompting.
            continue

def generate_random_number(max_value):
    """
    Generates a random integer between 1 and max_value (inclusive).
    This serves as the target number for the user to guess.
    """
    return random.randint(1, max_value)

def run_guessing_game(target):
    """
    Manages the guessing game, prompting the user to guess the target number
    and providing feedback until the correct number is guessed.
    """
    while True:
        user_guess = get_validated_input("Guess: ")  # Validate the guess as a positive integer.
        if user_guess < target:
            print("Too small!")
        elif user_guess > target:
            print("Too large!")
        else:
            print("Just right!")
            break  # Exit the loop when the guess is correct.
        
if __name__ == "__main__":
    main()
