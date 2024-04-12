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
        numerator, denominator = map(int, fraction.split('/'))
        if denominator == 0:
            raise ZeroDivisionError("Denominator cannot be zero.")
        if numerator > denominator:
            raise ValueError("Numerator must not be larger than denominator.")
        if numerator < 0 or denominator < 0:
            raise ValueError("Negative numbers are not allowed.")
    except ValueError:
        raise ValueError("Please enter both numerator and denominator as integers.")
    percentage = round((numerator / denominator) * 100)
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
