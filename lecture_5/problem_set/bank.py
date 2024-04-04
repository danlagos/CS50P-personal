def main():
    greeting = input("Greeting: ")
    print(check_greeting(greeting))

def check_greeting(greeting):
    if greeting.startswith("Hello"):
        return "$0"
    elif  greeting.startswith("h") or greeting.startswith("H"):
        return "$20"
    else:
        return "$100"
    
main()