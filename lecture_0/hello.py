def main(): 
    name = input("what is your name? ")
    hello(name)

def hello(to='world'):
    print(f"Hello, {to}")
    
main()