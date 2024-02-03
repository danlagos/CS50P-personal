"""
standard paradigm.  When you want the user to do something before
you get to the rest of the code.
while True:
    n = int(input("What is n? "))
    if n > 0:
        break
    
for _ in range(n):
    print("meow")
"""
"""
_summary_
usage of standard paradigm explained above.  Difference here is that 
this is dynamic and uses the def main() paradigm in python
"""
def main():
    number = get_number()
    meow(number)

def get_number():
    while True:
        n = int(input("What is n? "))
        if n > 0:
            return n

def meow(n):
    for _ in range(n):
        print("meow")
        
main()

