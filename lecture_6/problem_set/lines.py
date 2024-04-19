import sys
import os

def main():
    """
    This serves as the entry point for your program. 
    - Retrieves command-line arguments using sys.argv.
    - Handles command-line arguments through the validate_arguments() function.
    - If validations pass (i.e., correct number of arguments, proper file type, file exists):
        - Processes the file with process_file() and captures the result (number of valid lines).
        - Calls output_result() with the result from process_file() to display the final output.
    - Handles any errors from validation by displaying appropriate error messages and exiting the program.
    """
    # Retrieve command-line arguments (excluding the script name itself, hence sys.argv[1:]).
    args = sys.argv[1:]

    # Validate arguments by passing them to the validate_arguments function.
    # Expect validate_arguments to raise SystemExit with appropriate error messages for any issues.
    validated_file_path = validate_arguments(args)
    
    # If validate_arguments returns without error, proceed to process the file.
    count_of_lines = process_file(validated_file_path)
    
    # Output the result of the file processing.
    output_result(count_of_lines)

def validate_arguments(args):
    """
    Checks and validates the command-line arguments provided to the script.
    - Ensures exactly one argument is provided. If not, exits with an appropriate error message.
    - Checks if the provided argument is a file with a '.py' extension to ensure it's a Python script.
      If not, exits with the message "Not a Python file."
    - Verifies the existence of the file using os.path.exists(). If the file does not exist, 
      exits with the message "File does not exist."
    - If all checks pass, returns the validated file path for further processing.
    - Handles exceptions gracefully, ensuring any error conditions lead to a clear, user-friendly exit message.
    """
    # Check if exactly one command-line argument is provided.
    if len(args) != 1:
        # If no arguments are provided or too many are provided, exit with a corresponding message.
        if len(args) == 0:
            sys.exit("Too few command-line arguments")
        else:
            sys.exit("Too many command-line arguments")
    
    # Store the first (and should be only) argument for clarity.
    file_path = args[0]

    # Check if the file has a '.py' extension.
    if not file_path.endswith('.py'):
        sys.exit("Not a Python file")

    # Verify the file exists using os.path.exists().
    if not os.path.exists(file_path):
        sys.exit("File does not exist")
    
    # If all checks are passed, return the validated file path.
    return file_path

def process_file(file_path):
    """
    Open and read the file line by line.
    Use string methods to determine if a line should be counted or skipped.
        Lines should be stripped of leading and trailing whitespace to accurately check for blank lines and comments.
        Implement logic to skip lines that are either entirely whitespace or start with # (after whitespace is stripped).
    Maintain a counter for valid lines of code, which are neither comments nor blank.
    """
    pass

def output_result(count_of_lines):
    """
    Takes input from process_file function
    Return the count of non-comment, non-blank lines to the console as the final output.
    """
    pass
