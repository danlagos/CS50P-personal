def main():
    numerator, denominator = take_input()
    fuel_gauge(numerator, denominator)
    
def take_input():
    while True:
        user_input = input("Fraction: ")
        try:
            numerator, denominator = map(int, user_input.split('/'))
            if is_fraction_valid(numerator, denominator):
                return numerator, denominator
            else:
                print("denominator cannot be zero, and numerator must not be larger than denominator")
        except ValueError:
            print("Please enter both numerator and denominator as integers.")


def is_fraction_valid(numerator, denominator):
    if ((numerator > denominator) or (denominator == 0) or (denominator < 0) or (numerator < 0)):
        print("denominator cannot be zero, denominator must be larger than numerator.  Cannot input negative numbers")
        return False
    else:
        return True

def fuel_gauge(numerator, denominator):
    fuel_in_tank = numerator/denominator
    
    if fuel_in_tank <= 0.01:
        print("E")
    elif fuel_in_tank >= 0.99:
        print("F")
    else:
        fuel_in_tank = round(fuel_in_tank*100)
        print(f"{fuel_in_tank}%")

main()