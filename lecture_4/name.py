from sys import argv

# check for errors
if len(argv) < 2:
    exit("Too few arguments")
    
for arg in argv[1:]:
    print("Hello, my name is", arg)
