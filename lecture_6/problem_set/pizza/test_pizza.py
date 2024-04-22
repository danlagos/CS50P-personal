# Unit test for handle_cli_arguments()

"""

Test for No Arguments:
    simulate: no command-line arguments provided,
    expect: the function to display "Too few command-line arguments." and exit the program using sys.exit(),
    failure message: "Expected sys.exit() with 'Too few command-line arguments.' but got a different response 
        or no exit."

Test for Exactly One Argument:
    simulate: exactly one command-line argument provided (e.g., "filename.csv"),
    expect: the function to return the filename "filename.csv",
    failure message: "Expected function to return the filename 'filename.csv' 
        but did not return correctly or returned an incorrect filename."

Test for More Than One Argument:
    simulate: more than one command-line argument provided (e.g., "filename.csv extra_arg"),
    expect: the function to display "Too many command-line arguments." and exit the program using sys.exit(),
    failure message: "Expected sys.exit() with 'Too many command-line arguments.' 
        but got a different response or no exit."

"""

# Unit tests for process_and_read_csv()

"""
Test for File Does Not Exist:
    simulate: validated filename provided does not point to an existing file,
    expect: the function to display "File does not exist." and exit the program using sys.exit(),
    failure message: "Expected sys.exit() with 'File does not exist.' but got a different response or no exit."

Test for Successful File Reading and Parsing:
    simulate: validated filename provided points to an existing, correctly formatted CSV file,
    expect: the function to successfully parse the CSV using csv.DictReader into a list of dictionaries 
        and return this list,
    failure message: "Expected function to return a list of dictionaries parsed from the CSV file but failed to do so."

"""

# Unit tests for display_data()

"""
Test for Proper Formatting and Display:
    simulate: providing processed data as a list of dictionaries,
    expect: the function to format the data using the 'grid' style from the tabulate function 
        and display it correctly,
    failure message: "Expected function to display data in 'grid' style using tabulate but 
        did not display correctly or used incorrect format."

"""