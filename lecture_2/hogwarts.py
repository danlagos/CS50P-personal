"""
_summary_
dict - allows you to associate KEYS with VALUES.
list - a set of multiple values
"""
students = [
    {"name": "Hermione", "house": "Gryffindor", "patronus": "Otter"},
    {"name": "Harry", "house": "Gryffindor", "patronus": "Stag"},
    {"name": "Ron", "house": "Gryffindor", "patronus": "Jack Russel Terrier"},
    {"name": "Draco", "house": "Slytherin", "patronus": None},
]
 
for student in students:
    print(student["name"], student["house"], student["patronus"], sep = ", ")