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
    list_of_names = []  # Initialize the list outside of the loop
    while True:
        try:
            name = input("Name: ")  # Get a single name input
            list_of_names.append(name)  # Append the name to the list
        except (EOFError, KeyboardInterrupt):
            break  # Exit the loop when Ctrl-D is pressed
    return list_of_names  # Return the list of names after exiting the loop

def format_output(list_of_names):
    """ 
    consider using inflect library here
    takes the list of names as input 
    returns a formatted string according to the rules given.
    rules given:  
        For one name, you simply return it; 
        for two, join them with "and"; 
        for three or more, join with commas and "and" for the last two names.
    example output:
        $ python adieu.py                                                               
        Name: Liesl                                                                     
        Name: Friedrich                                                                 
        Name: Louisa                                                                    
        Name:                                                                           
        Adieu, adieu, to Liesl, Friedrich, and Louisa   
    """
    pass

if __name__ == "__main__":
    main()
