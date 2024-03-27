import inflect

def main ():
    """
    calls take_input() and stores in list_of_names
    call format_output(list_of_names) update in list_of_names
    print farewell message:  With the formatted list_of_names, prepare the final message to be printed to the console. Ensure it starts with "Adieu, adieu, to " followed by the formatted names
    """
    pass

def take_input():
    """
    Prompt the user for names in a loop.
    Handle EOFError to break the loop when Ctrl-D is pressed.
    Store and return the names in a list.
    """
    pass

def format_output(list_of_names):
    """ 
    consider using inflect library
    takes the list of names as input 
    returns a formatted string according to the rules given (using commas and "and" appropriately).
    """
    pass

if __name__ == "__main__":
    main()
