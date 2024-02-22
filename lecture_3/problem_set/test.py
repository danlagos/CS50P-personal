from collections import Counter

my_list = ['apple', 'banana', 'apple', 'orange', 'banana', 'apple']
counter = Counter(my_list)
print(counter)

print(counter['apple'])  # Outputs the number of occurrences of 'apple'

counter.update(['banana', 'orange'])
print(counter)