import sys
from pyfiglet import Figlet
from random import choice

def main():
    """
    Contains the conditional logic to decide whether to use a random font or a specific font based on command-line arguments.
    Calls the function to parse command-line arguments and retrieve the font name if specified.
    Calls the function to accept user input (the text to be transformed).
    Determines which font to use (random or specific) and sets it using pyfiglet.
    Renders the text in the chosen font and displays the output.
    """
    figlet = Figlet()
    fonts = figlet.getFonts()
    
    if len(sys.argv) == 1:
        random_font = choice(fonts)
        figlet.setFont(font=random_font)
        user_input = take_input()
        print(figlet.renderText(user_input))
    elif len(sys.argv) == 3:
        pass


def take_input():
    user_input = input("Input: ")
    return user_input

def parse_cli_arguments():
    """
    Checks if the correct number of arguments is provided (either 0 or 2 for this specific use case).
    If two arguments are provided, it validates the first argument to ensure it's either -f or --font and checks that the second argument corresponds to a valid font name.
    Depending on the validation, it either returns the font name specified by the user or signals to use a random font.
    In case of incorrect arguments, it exits the program with an error message using sys.exit.
    """
    pass

if __name__ == "__main__":
    main()