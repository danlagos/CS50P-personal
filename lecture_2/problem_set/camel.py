"""
turn filenames from camel case to snake case
"""
def main():
    camel_case_name = input("camelCase: ")
    snake_case_name = convert_to_snake_case(camel_case_name)
    print(snake_case_name)

def convert_to_snake_case(name):
    # Initialize an empty string for the snake case result
    snake_case = ""
    
    for index, letter in enumerate(name):
        # If the letter is uppercase and it's not the first character, add an underscore
        if letter.isupper() and index != 0:
            snake_case += "_"
        
        # Add the lowercase version of the current letter
        snake_case += letter.lower()

    return snake_case

main()
