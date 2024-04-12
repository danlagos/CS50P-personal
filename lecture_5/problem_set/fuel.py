def main():
    numerator, denominator = take_input()
    result = fuel_gauge(numerator, denominator)
    print(result)  # Move the print statement to the main function.

def take_input():
    while True:
        user_input = input("Fraction: ")
        try:
            numerator, denominator = map(int, user_input.split('/'))
            if denominator == 0:
                print("Denominator cannot be zero.")
            elif numerator > denominator:
                print("Numerator must not be larger than denominator.")
            elif numerator < 0 or denominator < 0:
                print("Negative numbers are not allowed.")
            else:
                return numerator, denominator
        except ValueError:
            print("Please enter both numerator and denominator as integers.")

def fuel_gauge(numerator, denominator):
    fuel_in_tank = numerator / denominator
    if fuel_in_tank <= 0.01:
        return "E"
    elif fuel_in_tank >= 0.99:
        return "F"
    else:
        return f"{round(fuel_in_tank * 100)}%"

if __name__ == "__main__":
    main()
