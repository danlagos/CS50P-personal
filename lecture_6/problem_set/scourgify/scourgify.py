import sys
import csv
import os

def main():
    """
    Orchestrates the workflow for transforming CSV file data:
    - Call handle_cli_arguments to get filenames. Store file names in variables: input_filename, output_filename.
    - Call validate_input_file with input_filename to check its existence and readability.
      Store the return value in variable validated_filename.
    - Call read_csv_file with validated_filename to read the data.
      Store the return value in variable data_dict.
    - Call process_data with data_dict to transform the data format.
      Store the return value in variable transformed_data.
    - Call write_to_output_csv with transformed_data and output_filename to write the new CSV file.
    """
    # Get input and output filenames from command-line arguments
    input_filename, output_filename = handle_cli_arguments()

    # Validate the input file
    validated_filename = validate_input_file(input_filename)

    # Read data from the validated input file
    data_dict = read_csv_file(validated_filename)

    # Process the data to transform names and rearrange into new format
    transformed_data = process_data(data_dict)

    # Write the transformed data to the output CSV file
    write_to_output_csv(transformed_data, output_filename)

def handle_cli_arguments():
    """
    Handles command-line arguments, ensuring the correct number of arguments for the program.

    :return: tuple containing the input filename and the output filename
    :rtype: tuple
    :raises SystemExit: If the number of arguments is incorrect
    """
    if len(sys.argv) < 3:
        sys.exit("Too few command-line arguments")
    elif len(sys.argv) > 3:
        sys.exit("Too many command-line arguments")
    # sys.argv[1] should be the input CSV filename and sys.argv[2] should be the output CSV filename
    return sys.argv[1], sys.argv[2]


def validate_input_file(input_filename):
    """
    Validates the existence and readability of a specified input file.
    
    :param input_filename: The name of the file to validate.
    :type input_filename: str
    :return: The input filename if the file exists and can be opened.
    :rtype: str
    :raises SystemExit: If the file does not exist or cannot be read.
    """
    # Check if the file exists
    if not os.path.exists(input_filename):
        sys.exit(f"Could not read {input_filename}")
    
    # Try to open the file to check readability
    try:
        with open(input_filename, 'r') as file:
            pass  # If we can open and close the file without error, it's considered valid
    except IOError:
        sys.exit(f"Could not read {input_filename}")
    
    return input_filename

def read_csv_file(validated_filename):
    """
    Reads data from a CSV file and converts it into a list of dictionaries, each representing a row.

    :param validated_filename: The name of the file to read, validated by a prior function to ensure existence and readability.
    :type validated_filename: str
    :return: A list of dictionaries where each dictionary represents a row from the CSV file.
    :rtype: list
    """
    with open(validated_filename, mode='r', newline='') as file:
        # Create a DictReader object
        reader = csv.DictReader(file)
        # Use a list comprehension to convert the reader object into a list of dictionaries
        return [row for row in reader]

def process_data(data_dict):
    """
    Processes data by splitting 'name' into 'first' and 'last' names and rearranging the dictionary.

    :param data_dict: List of dictionaries where each dictionary represents a row from a CSV with at least 'name' and 'house' keys.
    :return: List of new dictionaries with 'first', 'last', and 'house' as keys.
    :rtype: list
    """
    transformed_data = []
    for row in data_dict:
        # Extract 'name' and 'house' from each dictionary.
        name = row['name']
        house = row['house']
        
        # Split the 'name' field into last name and first name.
        # Assuming the format "Last, First"
        last_name, first_name = name.split(', ')
        
        # Create a new dictionary with 'first', 'last', and 'house'.
        new_dict = {
            'first': first_name,
            'last': last_name,
            'house': house
        }
        
        # Append the new dictionary to the transformed data list.
        transformed_data.append(new_dict)
    
    return transformed_data

def write_to_output_csv(transformed_data, output_filename):
    """
    Writes a list of dictionaries to a CSV file using the specified filename.

    :param transformed_data: List of dictionaries where each dictionary represents a row to be written to the CSV.
    :param output_filename: The name of the file to which the CSV data will be written.
    """
    # Define the fieldnames from the keys of the first dictionary, assuming all dictionaries have the same keys
    fieldnames = ['first', 'last', 'house']  # This can be dynamic based on data: fieldnames = transformed_data[0].keys() if transformed_data else []

    # Open the file in write mode with newline='' to prevent writing extra blank lines in the output file
    with open(output_filename, mode='w', newline='') as file:
        writer = csv.DictWriter(file, fieldnames=fieldnames)

        # Write the header (column names)
        writer.writeheader()

        # Iterate over each data row and write it to the CSV
        for row in transformed_data:
            writer.writerow(row)

if __name__ == "__main__":
    main()
