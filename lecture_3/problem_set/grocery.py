def main():
    """
    Execute the program workflow:
    1. Collect user input of grocery items until EOFError is caught.
    2. Count occurrences of each item, considering case-insensitivity.
    3. Sort the counted items alphabetically by their names and convert names to uppercase.
    4. Print the sorted list of items, prefixed with their counts.
    """
    
    grocery_list = collect_user_input()
    grocery_list = count_occurrences(grocery_list)
    grocery_list = sort_and_prepare_output(grocery_list)
    
    print_sorted_list(grocery_list)

def collect_user_input():
    """
    Collect user inputs for grocery items in a loop until EOFError (or KeyboardInterrupt) is caught.
    - Inputs are collected line by line.
    - Each input is appended to a list.
    - The function returns the list of user inputs.
    """
    
    grocery_list = []
    
    while True:
        try:
            user_inputs = input()
            grocery_list.append(user_inputs)
        except (EOFError, KeyboardInterrupt):
            return grocery_list

def normalize_input(grocery_list_item):
    """
    Normalize a single grocery list item by converting it to lowercase.
    - This ensures case-insensitive comparison and counting.
    - Returns the normalized string.
    """
    
    return grocery_list_item.lower()

def count_occurrences(grocery_list):
    """
    Count the occurrences of each item in the provided grocery list.
    - Each item is first normalized to lowercase to ensure case-insensitive counting.
    - Utilizes the Counter class to efficiently count occurrences.
    - Returns a dictionary with items as keys and their counts as values, converted from a Counter object for compatibility.
    """
    
    from collections import Counter

    normalized_grocery_list = [normalize_input(item) for item in grocery_list] 
    grocery_dictionary = Counter(normalized_grocery_list)
    
    return dict(grocery_dictionary)

def sort_and_prepare_output(unsorted_grocery_dictionary):
    """
    Sorts the provided dictionary of grocery items and converts item names to uppercase.
    - Sorting is done alphabetically based on item names (keys).
    - Returns a new dictionary with uppercase keys and original counts preserved.
    """
    
    sorted_dict = {key: unsorted_grocery_dictionary[key] for key in sorted(unsorted_grocery_dictionary)}
    return {key.upper(): sorted_dict[key] for key in sorted_dict}

def print_sorted_list(sorted_grocery_dictionary):
    """
    Prints items from the provided sorted dictionary, with each item's count followed by its name.
    - The item name (key) is expected to be in uppercase.
    - Output format for each item: "count item_name".
    """
    
    for key, value in sorted_grocery_dictionary.items():
        print(f"{value} {key}")

main()