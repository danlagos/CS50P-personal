students = []

with open("students.csv") as file:
    for line in file:
        name , house = line.strip().split(",")
        student = {"name" : name, "house" : house}
        students.append(student)

def get_name(student):
    return student["name"]

def get_house(student):
    return student["house"]

for student in sorted(students, key=get_name, reverse=True):
    print(f"{student['name']} is in {student['house']}")