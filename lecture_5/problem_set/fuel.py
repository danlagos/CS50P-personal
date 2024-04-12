def main():
    fraction = input("Fraction: ")
    try:
        percentage = convert(fraction)
        result = gauge(percentage)
        print(result)
    except (ValueError, ZeroDivisionError) as e:
        print(e)

def convert(fraction):
    try:
        parts = fraction.split('/')
        if len(parts) != 2:
            raise ValueError("Input must be in X/Y format.")
        numerator, denominator = map(int, parts)  # This may raise ValueError if conversion fails
    except ValueError:
        raise ValueError("Please enter both numerator and denominator as integers.") from None

    if denominator == 0:
        raise ZeroDivisionError("Denominator cannot be zero.")
    if numerator > denominator:
        raise ValueError("Numerator must not be larger than denominator.")
    if numerator < 0 or denominator < 0:
        raise ValueError("Negative numbers are not allowed.")

    percentage = round((numerator / denominator) * 100)
    # this introduces an error.  I expect test_convert_valid_input to fail in test_fuel.py
    # return str(max(0, min(100, percentage)))  # Mistakenly return a string instead of an integer
    return max(0, min(100, percentage))  # Ensure the percentage is clamped between 0 and 100.




def gauge(percentage):
    if percentage <= 1:
        return "E"
    elif percentage >= 99:
        return "F"
    else:
        return f"{percentage}%"

if __name__ == "__main__":
    main()
