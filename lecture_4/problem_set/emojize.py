import emoji

def main():
    """
    call take_input() and place input in variable
    produce output with emoji, if emoji command is present.  Allow for aliases.
    """
    user_input = take_input()
    print("Output: " + emoji.emojize(user_input, language='alias'))

def take_input():
    user_input = input("Input: ")
    return user_input    

if __name__ == "__main__":
    main()
   