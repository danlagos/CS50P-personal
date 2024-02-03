def main():
    processed_input = process_input()
    print(processed_input)
    
def process_input():
    x = input("Please provide input! ")
    words = x.split()  # Splitting the input string into words
    return '...'.join(words)  # Joining the words with '...'

main()
