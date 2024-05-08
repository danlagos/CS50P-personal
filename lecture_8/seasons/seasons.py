from datetime import date
import inflect
import sys

def main():
    """
    - Orchestrates the flow of the program.
    - Use input() to prompt the user for their date of birth in the specified format (YYYY-MM-DD).
    - Implement input validation to check if the input is in the correct format. 
        -  Use a try-except block to attempt parsing the date with datetime.strptime(). 
        -  If an exception is raised, use sys.exit() to terminate the program with a message 
        indicating the date is invalid.
    """
    ...


def calculate_date():
    """
    - Convert the string to a date object.
    - Retrieve today's date using date.today().
    - Calculate the difference between today's date and the entered birthdate to get a 
    timedelta object.
    - Extract the total days from the timedelta object and convert this to minutes 
    (multiply by 1440, the number of minutes in a day).
    """
    ...


def convert_date_to_words():
    """
    - Initialize an inflect engine.
    - Convert the total minutes number into words using the inflect method appropriate for 
    converting numbers to words.
    - Print this string to the console as per the format seen in the video.
    """
    ...


if __name__ == "__main__":
    main()