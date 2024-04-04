def main():
    word = prompt_input()
    converted_message = shorten(word)
    print(provide_output(converted_message))

def prompt_input():  
    # asks for input from user
    tweet = input("Input: ")
    return tweet

def shorten(word):
    if not isinstance(word, str):
        raise TypeError("Input must be a string")
    tweet = ""
    for letter in word:
        if letter.lower() not in "aeiou":
            tweet += letter
    return tweet

def provide_output(converted_message):
    # returns converted message
    return f"Output: {converted_message}"

if __name__ == "__main__":
    main()