import random

def main():
    # Get the level from the user, ensuring it's a positive integer.
    level = get_validated_input("Level: ")
    
    # Generate a random target number within the specified level.
    target_number = generate_random_number(level)
    
    # Run the guessing game loop.
    run_guessing_game(target_number)

def get_validated_input(prompt):
    """
    Repeatedly prompt the user with the given prompt until a valid positive integer is entered.
    For level input, validate that it's a positive integer.
    For guess input, additionally handle the case where the guess could be outside the valid range, if necessary.
    Return the validated integer.
    """
    while True:
        user_input = input(prompt)  # Take input as a string.
        try:
            # Attempt to convert the input to an integer.
            user_input_as_int = int(user_input)
            if (user_input_as_int <=0):
                continue
            return user_input_as_int  # Return the converted integer.
        except ValueError:
            # If conversion fails continue the loop.
            continue
        
def generate_random_number(max_value):
    """
    Generate a random number between 1 and max_value (inclusive) using the random module.
    Return this number as the target for the game.
    """
    return random.randint(1, max_value)
    
def run_guessing_game(target):
    """
    Prompt the user to guess the target number, providing feedback for each guess.
    Tell the user if their guess is too small, too large, or just right.
    Repeat until the correct guess is made.
    """
    while True:
        # Prompt user for a guess and validate it's a positive integer
        user_guess = get_validated_input("Guess: ")
        # If guess is smaller than target, inform the user it's too small.
        if user_guess < target:
            print("Too small!")
        # If guess is larger than target, inform the user it's too large.
        elif user_guess > target:
            print("Too large!")
        # If guess matches the target, congratulate the user and break the loop.
        elif user_guess == target:
            print("Just right!")
            break
        
if __name__ == "__main__":
    main()
