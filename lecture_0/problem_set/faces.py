"""
link for prpblem set
https://cs50.harvard.edu/python/2022/psets/0/faces/
"""

def main():
    message = input()
    print(convert(message))
    
def convert(input_str):
    # Replace :) with 🙂
    result = input_str.replace(":)", "🙂")
    
    # Replace :( with 🙁
    result = result.replace(":(", "🙁")

    return result

main()