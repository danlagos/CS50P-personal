def main():
    numerator, denominator = take_input()
    fuel_gauge(numerator, denominator)
    
def take_input():
    try:
        numerator, denominator = input("Fraction: ").split('/')
        # Convert to integers to validate input
        numerator = int(numerator)
        denominator = int(denominator)
    except ZeroDivisionError:
        pass
    
    while check_input_numerator(numerator, denominator) == False:
        numerator, denominator = input("Fraction: ").split('/')
        numerator = int(numerator)
        denominator = int(denominator)
        
    return numerator, denominator

def check_input_numerator(numerator, denominator):
    if numerator < 0 or denominator <= 0:
        print("Invalid input")
        return False

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