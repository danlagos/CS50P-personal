with open("students.csv") as file:
    for line in file:
        name, house = line.strip().split(",")
        print(f"{name} is in {house}")

