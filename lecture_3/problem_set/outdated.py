import re

def main():
    """
    Start a loop that continues until a valid date is successfully processed.
    Call get_user_input() and store the returned value in a variable.
    Call parse_date() with the user input as an argument. Store the returned date components (if any) in a variable.
    If parse_date() successfully returns date components (indicated by a non-error state), call format_date() with these components.
    Print the returned value from format_date(), which should be the date in "YYYY-MM-DD" format.
    Break the loop, ending the program, if the date has been successfully formatted. Otherwise, continue prompting the user.
    """
    while True:
        user_input = get_user_input()
        date_components = parse_date(user_input)
        if date_components:
            formatted_date = format_date(date_components)
            print(formatted_date)
            break

def get_user_input():
    """
    Prompt the user for a date input.
    Return the user's input.
    """
    # Prompt the user and capture the input
    user_date = input("Date: ")
    # Return the captured input
    return user_date

def parse_date(user_input):
    # Define regex patterns for both date formats
    numeric_date_pattern = re.compile(r"(\d{1,2})/(\d{1,2})/(\d{4})")
    textual_date_pattern = re.compile(r"([a-zA-Z]+) (\d{1,2}), (\d{4})")

    # List of month names to help convert textual month to numeric
    months = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]

    # Check for numeric "MM/DD/YYYY" format
    numeric_match = numeric_date_pattern.match(user_input)
    if numeric_match:
        month, day, year = numeric_match.groups()
        month, day, year = int(month), int(day), int(year)
        # Validate the components (e.g., month is between 1 and 12)
        if 1 <= month <= 12:
            return {"month": month, "day": day, "year": year}
    
    # Check for "Month DD, YYYY" format
    textual_match = textual_date_pattern.match(user_input)
    if textual_match:
        month_name, day, year = textual_match.groups()
        day, year = int(day), int(year)
        if month_name in months:
            month = months.index(month_name) + 1  # Convert month name to its numeric equivalent
            return {"month": month, "day": day, "year": year}

    # If neither format matches, return an error state or None
    return None

def format_date(date_components):
    """
    Extract year, month, and day from the date components.
    Format the date in YYYY-MM-DD format, ensuring month and day are zero-padded to two digits.
    Return the formatted date string.
    """
    # Extract year, month, and day from the date components
    year = date_components["year"]
    month = date_components["month"]
    day = date_components["day"]

    # Format the date in YYYY-MM-DD format, zero-padding month and day as needed
    formatted_date = f"{year:04d}-{month:02d}-{day:02d}"

    # Return the formatted date string
    return formatted_date

if __name__ == "__main__":
    main()