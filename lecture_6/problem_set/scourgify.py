import sys
import csv

def main():
    """
    - handle CLI arguments
    - Before proceeding with any data processing validate input file    
    """
    pass

def handle_cli_arguments():
    """
    - what is my input?
    - Check the number of command-line arguments provided using sys.argv. 
    - Ensure there are exactly three arguments: the script name, the input CSV filename, 
        and the output CSV filename.
    - Define error messages for "Too few command-line arguments" and "Too many command-line arguments" and use sys.exit to terminate the program with these messages if the number of arguments is incorrect.
        - what do I output
    """
    pass

def validate_input_file():
    """
    - what is my input?
    -check if the input file exists and can be opened. 
        If not, exit the program using sys.exit with an error message indicating the file could not be read.
    - what do I output
    """    
    pass

def read_csv_file():
    """
    - what is my input?
    - use csv module to open and read csv file
    - use DictReader to access columns by header names
    - return dictionary with columns and header names
    """
    pass

def process_data():
    """
    - what is my input?
    - for each row in csv file, split name field into last and first name
    - create new dictionary for each row
        map first name, last name, and house to corresponding values from input data
    - return dictionary in new format
    """
    pass

def write_to_output_csv():
    """
    - input:  dictionary from process_data()
    - open a new csv file using context manager
    - write header first, using 'writeheader()' method of 'DictWriter'
    - for each row add contents of dictionary
    - output:  new csv file, how do I capture the name of the new file?  New name is given in args.
    """
    pass