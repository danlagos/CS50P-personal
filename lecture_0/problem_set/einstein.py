def main():
    user_mass = int(input("m: "))
    print(f"e:  {emc2(user_mass)}")

def emc2(m):
    return m * 300000000 **2
    
main()