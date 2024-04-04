def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")

def is_valid(s):
    check_1 = s[0:2].isalpha() # ensure starts with 2 letters
    check_2 = 6 >= len(s) >= 2 # maximum 6 char and min of 2 char
    check_3 = all(letter.isalpha() or letter.isdigit() for letter in s) # no punctuation
    check_4 = False # initialize variable that will check if numbers are at the end and first number is not '0'
    
    # Find the first digit in the string
    first_digit_index = next((index for index, letter in enumerate(s) if letter.isdigit()), len(s))
    
    # Check if all characters before the first digit are letters and all characters after are digits
    if s[:first_digit_index].isalpha() and (s[first_digit_index:].isdigit() or first_digit_index == len(s)):
        # Check if the first digit is not '0'
        if first_digit_index == len(s) or s[first_digit_index] != '0':
            check_4 = True

    return check_1 and check_2 and check_3 and check_4

if __name__ == "__main__":
    main()