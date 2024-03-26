import sys
from pyfiglet import Figlet
from random import choice

def main():
    figlet = Figlet()
    fonts = figlet.getFonts()

    font_name = parse_cli_arguments(fonts)  # Adjusted to pass available fonts for validation

    # Set the font based on the name determined above
    figlet.setFont(font=font_name)

    # Prompt the user for input text and render it using the selected font
    user_input = take_input()
    print(figlet.renderText(user_input))

def take_input():
    """Prompt the user for text input."""
    return input("Input: ")

def parse_cli_arguments(fonts):
    """
    Parses command-line arguments to validate the font flag and font name.
    Checks if the specified font is among the available fonts.
    Exits with an error message if the arguments are invalid or the font is not available.
    """
    if len(sys.argv) == 1:
        return choice(fonts)  # Select and return a random font if no arguments are provided
    elif len(sys.argv) == 3 and (sys.argv[1] == "-f" or sys.argv[1] == "--font"):
        if sys.argv[2] in fonts:
            return sys.argv[2]  # Return the specified font name if valid
        else:
            sys.exit("Invalid usage")  # Font specified is not valid
    else:
        sys.exit("Invalid usage")  # Arguments do not match the expected pattern

if __name__ == "__main__":
    main()
