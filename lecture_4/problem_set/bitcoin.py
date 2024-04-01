import requests
import sys
import json

def main():
    """
    Orchestrate the program's flow:
    - Validate the command-line argument for the number of Bitcoins.
    - Fetch the current Bitcoin price from the CoinDesk API.
    - Parse the API response to extract the Bitcoin price in USD.
    - Calculate and output the total cost for the specified amount of Bitcoin.
    Coordinate data flow and result presentation within the program.
    """
    number_of_bitcoin = validate_cli_arg()
    bitcoin_price_data = fetch_bitcoin_data()
    current_bitcoin_price = parse_api_response(bitcoin_price_data)
    calculate_and_format_price(number_of_bitcoin, current_bitcoin_price)

def validate_cli_arg():
    """
    Validate the command-line argument:
    - Ensure exactly one numerical argument is provided for the number of Bitcoins.
    - Exit with an error message if the argument is missing or not a valid number.
    Return the validated number of Bitcoins as a float.
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
    Fetch the current market price of Bitcoin from the CoinDesk API.
    Handle request errors gracefully and exit with a message if the request fails.
    Return the API response as a JSON object containing Bitcoin price information.
    """
    try:
        response = requests.get('https://api.coindesk.com/v1/bpi/currentprice.json')
        bitcoin_price_data = response.json()
    except requests.RequestException:
        sys.exit("request failed")
    return bitcoin_price_data

def parse_api_response(bitcoin_price_data):
    """
    Extract the Bitcoin price in USD from the provided API JSON response.
    Parameter:
    - bitcoin_price_data: JSON object containing Bitcoin pricing information.
    Return the Bitcoin price in USD as a float.
    """
    current_bitcoin_price = bitcoin_price_data["bpi"]["USD"]["rate_float"]
    return current_bitcoin_price

def calculate_and_format_price(number_of_bitcoin, current_bitcoin_price):
    """
    Calculate the total cost for a specified amount of Bitcoin and format the output.
    Parameters:
    - number_of_bitcoin: The desired amount of Bitcoin to calculate for (float).
    - current_bitcoin_price: The current price of Bitcoin in USD (float).
    Output the formatted cost to four decimal places, with a comma as the thousands separator.
    """
    amount = number_of_bitcoin * current_bitcoin_price
    print(f"${amount:,.4f}")

if __name__ == "__main__":
    main()