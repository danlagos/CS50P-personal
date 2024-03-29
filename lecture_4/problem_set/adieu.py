import inflect

def main():
    """
    Main function to orchestrate the process:
    1. Calls take_input() to collect names from the user.
    2. Calls format_output() with the list of collected names to get a grammatically correct, formatted string.
    3. Prints the farewell message with the formatted names.
    """
    list_of_names = take_input()
    formatted_names = format_output(list_of_names)
    print(f"Adieu, adieu, to {formatted_names}")

def take_input():
    """
    Collects names from the user in a loop. It prompts the user for names, one at a time.
    The loop is terminated by the user pressing Ctrl-D (EOFError) or Ctrl-C (KeyboardInterrupt), signaling the end of input.
    Stores the names in a list and returns this list at the end.
    
    Returns:
        list_of_names (list): A list of names entered by the user.
    """
    list_of_names = []  # Initialize the list to store names
    while True:
        try:
            name = input("Name: ")  # Prompt for a single name
            if name:  # Only append non-empty names to the list
                list_of_names.append(name)
        except (EOFError, KeyboardInterrupt):  # Catch termination signals
            break  # Exit the loop when termination signal is received
    return list_of_names  # Return the collected names

def format_output(list_of_names):
    """
    Formats a list of names into a grammatically correct string using the inflect library.
    This function handles different cases:
    - For one name, it returns just the name.
    - For two names, it joins them with "and".
    - For three or more names, it joins them with commas and "and" before the last name.
    
    Parameters:
        list_of_names (list): The list of names to format.
    
    Returns:
        formatted_names (str): A string of formatted names.
    """
    # Initialize the inflect engine
    p = inflect.engine()
    
    # Use the engine to join the list of names into a formatted string
    formatted_names = p.join(list_of_names)
    
    # Return the formatted string
    return formatted_names

if __name__ == "__main__":
    main()
