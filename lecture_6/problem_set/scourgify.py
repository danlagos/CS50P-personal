import sys
import csv

def main():
    """
    - Call handle_cli_arguments to get filenames. Store file names in variables: input_filename, output_filename.
    - Call validate_input_file with input_filename to check its existence and readability.
      Store the return value in variable validated_filename.
    - Call read_csv_file with validated_filename to read the data.
      Store the return value in variable data_dict.
    - Call process_data with data_dict to transform the data format.
      Store the return value in variable transformed_data.
    - Call write_to_output_csv with transformed_data and output_filename to write the new CSV file.
    """
    pass

def handle_cli_arguments():
    """
    - Input: args from command line (sys.argv)
    - Use len(sys.argv) to:
        - Check the number of command-line arguments provided.
        - Ensure there are exactly three arguments: the script name, the input CSV filename, 
            and the output CSV filename.
    - Define and handle error messages for "Too few command-line arguments" and "Too many command-line arguments" 
        using sys.exit to terminate the program with these messages if the number of arguments is incorrect.
    - Return both input_filename and output_filename if the arguments are correct.
    """
    pass

def validate_input_file(input_filename):
    """
    - Input: input_filename from handle_cli_arguments
    - Check if the input file exists and can be opened. If not, exit the program using sys.exit 
      with an error message indicating the file could not be read: 'Could not read <name of file>.csv'
    - Return input_filename if validation is successful; this confirms the file is ready to be read.
    """
    pass

def read_csv_file(validated_filename):
    """
    - Input: validated_filename from validate_input_file
    - Use the csv module to open and read the CSV file within a context manager to ensure proper handling of file resources.
    - Use csv.DictReader to access columns by header names, facilitating easy data manipulation.
    - Return a list of dictionaries, each representing a row from the CSV.
    """
    pass

def process_data(data_dict):
    """
    - Input: data_dict from read_csv_file()
    - Iterate over each row in the data_dict, split the 'name' field into 'last' and 'first' names.
    - Create a new dictionary for each row mapping 'first name', 'last name', and 'house' to corresponding values from the input data.
    - Return a list of these new dictionaries formatted for the output.
    """
    pass

def write_to_output_csv(transformed_data, output_filename):
    """
    - Input: transformed_data from process_data(), and output_filename from handle_cli_arguments
    - Open a new CSV file using a context manager to handle the file opening, writing, and closing safely.
    - Use csv.DictWriter with the fieldnames as ['first', 'last', 'house']. Call 'writeheader()' method to write the column headers.
    - Iterate over each row in transformed_data and use 'writerow()' to add contents to the CSV.
    - Output: The function writes to a new CSV file named as per output_filename, successfully creating the desired output file.
    """
    pass

if __name__ == "__main__":
    main()
