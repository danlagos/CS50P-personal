from datetime import datetime, timedelta
import inflect
import sys

def main():
    """
    Orchestrates the flow of the program by prompting the user for their date of birth,
    validating the format, and calculating the time since then in minutes, finally
    printing the age in minutes in a formatted string as per requirements.

    :raises SystemExit: If the date format is invalid, it terminates the program and
                        indicates the error in the date input.
    """
    # Prompt user for their date of birth
    user_input = input("Please enter your date of birth (YYYY-MM-DD): ")

    try:
        # Try to parse the date, raise SystemExit if invalid format
        minutes = calculate_date(user_input)
    except ValueError as e:
        print(e)
        sys.exit(1)  # Exit the program indicating an error

    # Pass the minutes to format_minutes_as_words and receive formatted string
    formatted_minutes = format_minutes_as_words(minutes)

    # Print the formatted string
    print(formatted_minutes)


def calculate_date(birthdate):
    """
    Calculates the difference in minutes from a given birthdate (at midnight) to today's 
    date at midnight.
    
    :param birthdate: The date of birth input by the user, expected in YYYY-MM-DD format.
    :type birthdate: str
    :return: Total number of minutes from the birthdate to today's date.
    :rtype: int
    :raises ValueError: If the birthdate is not a valid date or not in the expected format.
    """
    try:
        # Convert the string input to a date object assuming the input is in the format YYYY-MM-DD
        birthdate = datetime.strptime(birthdate, '%Y-%m-%d').date()

        # Get today's date adjusted to midnight
        today = datetime.now().date()

        # Calculate the timedelta between today and the birthdate
        delta = today - birthdate

        # Convert timedelta days to minutes (multiply days by 1440, which is the number of minutes in a day)
        minutes = delta.days * 1440

        return minutes
    except ValueError as e:
        # Raise an error if the input date format is incorrect or the date is invalid
        raise ValueError("Invalid date format. Please enter the date in YYYY-MM-DD format.") from e


def format_minutes_as_words(minutes):
    """
    Converts a given number of minutes into words, formatted without conjunctions,
    expressing numbers as full words and phrases in a continuous flow, 
    without using numerical digits or conjunctions like 'and.'

    :param minutes: Total number of minutes to be converted.
    :type minutes: int
    :return: The minutes expressed in words, formatted as specified (e.g., "Five hundred twenty-five thousand, six hundred minutes").
    :rtype: str
    """
    # Initialize an inflect engine
    p = inflect.engine()
    
    # Convert the integer minutes to words using the inflect engine
    # Use the number_to_words method to convert the number into words
    # Specify `andword=''` to avoid using "and" in the number phrase
    words = p.number_to_words(minutes, andword='')
    
    # Ensure the formatting adheres to the assignment specification
    # Capitalize the first letter and append ' minutes' at the end to form the full phrase
    result = words[0].upper() + words[1:] + " minutes"

    # Return the formatted string
    return result


if __name__ == "__main__":
    main()
