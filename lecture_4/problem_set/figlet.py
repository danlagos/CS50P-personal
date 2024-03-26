import sys
from pyfiglet import Figlet
from random import choice

def main():
    figlet = Figlet()
    fonts = figlet.getFonts()

    # If no arguments, use a random font; else, parse CLI arguments for font selection
    if len(sys.argv) == 1:
        font_name = choice(fonts)  # Select a random font if no arguments are provided
    else:
        font_name = parse_cli_arguments()  # This will handle argument parsing and validation

    # Set the font based on the name determined above
    if font_name in fonts:
        figlet.setFont(font=font_name)
    else:
        sys.exit(f"Error: The font '{font_name}' is not available.")

    # Prompt the user for input text and render it using the selected font
    user_input = take_input()
    print(figlet.renderText(user_input))

def take_input():
    """Prompt the user for text input."""
    return input("Input: ")

def parse_cli_arguments():
    """
    Parses command-line arguments to validate the font flag and font name.
    Returns the font name if specified and valid; exits with an error if invalid.
    """
    if len(sys.argv) == 3 and (sys.argv[1] == "-f" or sys.argv[1] == "--font"):
        return sys.argv[2]  # Return the font name specified by the user
    else:
        sys.exit("Usage: python figlet.py [-f --font] [fontname]")

if __name__ == "__main__":
    main()
