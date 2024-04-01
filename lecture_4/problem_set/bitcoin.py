import requests
import sys
import json

def main():
    """ 
    Orchestrates the program's flow:
    - Validates the command-line argument for the number of Bitcoins to calculate.
    - Fetches the latest Bitcoin price from an external API.
    - Parses the API response to extract the Bitcoin price.
    - Calculates the cost of the specified amount of Bitcoin.
    - Outputs the calculated cost in a user-friendly format.
    Ensures smooth coordination between different parts of the program, handling data passing and result presentation.
    """
    number_of_bitcoin = validate_cli_arg()
    bitcoin_price_data = fetch_bitcoin_data()
    current_bitcoin_price = parse_api_response(bitcoin_price_data)
    calculate_and_format_price(number_of_bitcoin, current_bitcoin_price)

def validate_cli_arg():
    """ 
    Checks if the program was called with a valid numerical argument representing the number of Bitcoins.
    - Ensures there's exactly one numerical argument provided.
    - Confirms the argument can be interpreted as a float (the amount of Bitcoin).
    If these conditions are not met, the program exits, displaying an appropriate error message to the user.
    Returns:
    - The number of Bitcoins as a float if validation succeeds.
    """
    if len(sys.argv) != 2:
        sys.exit("Missing command-line argument")
        
    try:
        number_of_bitcoin = float(sys.argv[1])
    except ValueError:
        sys.exit("Command-line argument is not a number")
    return number_of_bitcoin

def fetch_bitcoin_data():
    """ 
    Contacts the CoinDesk Bitcoin Price Index API to obtain the current market price of Bitcoin.
    Implements error handling to gracefully manage any issues with the API request, such as network errors.
    Returns:
    - A JSON object from the API containing the latest Bitcoin price information.
    """
    try:
        response = requests.get('https://api.coindesk.com/v1/bpi/currentprice.json')
        bitcoin_price_data = response.json()
    except requests.RequestException:
        sys.exit("request failed")
    return bitcoin_price_data

def parse_api_response(bitcoin_price_data):
    """ 
    Extracts the Bitcoin price in USD from the API's JSON response.
    Parameters:
    - The API response in JSON format, containing Bitcoin pricing information.
    Carefully navigates the JSON structure to locate and return the current price of Bitcoin.
    Returns:
    - The price of Bitcoin as a float.
    """
    current_bitcoin_price = bitcoin_price_data["bpi"]["USD"]["rate_float"]
    return current_bitcoin_price

def calculate_and_format_price(number_of_bitcoin, current_bitcoin_price):
    """ 
    Utilizes the current Bitcoin price and the desired amount (in Bitcoins) to calculate total cost.
    - Computes the cost based on the user-specified amount and the latest price.
    - Formats the result to match currency standards (e.g., comma as thousands separator, four decimal places).
    Parameters:
    - Number of Bitcoins desired (float).
    - Current price of Bitcoin (float).
    Outputs the formatted string directly or returns it for display, depending on implementation preference.
    """
    amount = number_of_bitcoin * current_bitcoin_price
    print(f"${amount:,.4f}")

if __name__ == "__main__":
    main()