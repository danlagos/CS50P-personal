

name = input("What is your name? ")

# this is the programing equivilant of someong double clicking on a file, editing, and saving it.
# w opens the file every time and writes to it. If the file does not exist, it will create it.
# appending to a file is done with "a"
# file = open("names.txt", "w")

with open("names.txt", "a") as file:
    file.write(f"{name}\n")
