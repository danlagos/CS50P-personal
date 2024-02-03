def main():
    message = prompt_input()
    converted_message = convert_input(message)
    provide_output(converted_message)

def prompt_input():  
    # asks for input from user
    tweet = input("Input: ")
    return tweet

def convert_input(message):
    # takes message.  returns message without vowels
    tweet = ""
    for letter in message:
        if letter not in ["a","e", "i", "o", "u", "A", "E", "I", "O", "U"]:
            tweet += letter

    return tweet

def provide_output(converted_message):
    # takes converted message and outputs in terminal
    print(f"Output: {converted_message}")

main()