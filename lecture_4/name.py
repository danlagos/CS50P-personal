from sys import argv

if len(argv) < 2:
    print("Too few arguments")
elif len(argv) > 2:
    print("Too many arguments")
else:
    print("Hello, my name is", argv[1])
