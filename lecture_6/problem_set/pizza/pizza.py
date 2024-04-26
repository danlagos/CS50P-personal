import sys
from tabulate import tabulate
import csv

def main():
    """
    Entry point that orchestrates the program's logic:
        - Retrieves and validates the filename from command line arguments.
        - Processes and reads the CSV file, returning structured data.
        - Displays the formatted data using tabulate.
    """
    # Retrieve and validate the filename from command line arguments
    filename = handle_cli_arguments()

    # Process and read the CSV file, returning structured data
    structured_data = process_and_read_csv(filename)

    # Display the formatted data using tabulate
    display_data(structured_data)

def handle_cli_arguments():
    """
    Checks and validates the command line arguments.
    Ensures exactly one argument is provided and checks for proper file extension:
        - If no arguments, display "Too few command-line arguments." and exit using sys.exit().
        - If more than one argument, display "Too many command-line arguments." and exit using sys.exit().
        - Check if the single argument provided ends with '.csv'. If not, display "Not a CSV file." and exit
            using sys.exit().
    Returns the filename if it is a valid single argument ending with '.csv'.
    """
    # sys.argv[0] is the script name and sys.argv[1:] are the actual arguments
    if len(sys.argv) < 2:
        print("Too few command-line arguments.")
        sys.exit(1)
    elif len(sys.argv) > 2:
        print("Too many command-line arguments.")
        sys.exit(1)
    else:
        filename = sys.argv[1]
        if not filename.endswith('.csv'):
            print("Not a CSV file.")
            sys.exit(1)
        return filename

def process_and_read_csv(validated_filename):
    """
    Opens and reads the CSV file using a context manager.
    Uses csv.DictReader to parse the file into a list of dictionaries:
        - Handles file existence errors by catching FileNotFoundError, displays "File does not exist." 
            and exits using sys.exit().
    Returns the list of dictionaries containing the file data once read successfully.
    """
    try:
        with open(validated_filename, mode='r', newline='') as file:
            reader = csv.DictReader(file)
            return list(reader)
    except FileNotFoundError:
        print("File does not exist.")
        sys.exit(1)

def display_data(processed_data):
    """
    Formats and displays the data using 'grid' style from the tabulate function.

    Args:
    processed_data (list of dict): A list of dictionaries where each dictionary represents a row of data.
    """
    if processed_data:
        # Automatically use the keys of the dictionaries as headers
        table = tabulate(processed_data, headers="keys", tablefmt='grid')
        print(table)
    else:
        print("No data available to display.")

if __name__ == "__main__":
    main()
