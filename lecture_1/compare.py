def main():
    x = int(input("what is x? "))
    y = int(input("what is y? "))
    
    if is_not_equal(x, y):
        print("x is not equal to y")
    else:
        print("x is equal to y")

def is_not_equal(x , y):
    if x != y:
        return True
    else:
        return False
    
main()
