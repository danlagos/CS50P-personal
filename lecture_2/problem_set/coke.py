""" 
coke machine and test
"""
def main():
    coke_machine()
    
def check_coin(payment):
    while True:
        if payment in [5, 10, 25]:
            return payment
        else:
            print("Please insert nickels, dimes, or quarters: ")
            payment = int(input("Insert Coin: "))

def insert_coin():
    payment = int(input("Insert Coin: "))
    payment = check_coin(payment)
    return payment
            
def coke_machine():
    total_amount = 50
    
    print(f"Amount Due: {total_amount}")
    payment = insert_coin()    
    amount_due = total_amount-payment
    print(f"Amount Due: {amount_due}" )
    
    while amount_due >= 0:
        payment = insert_coin()
        amount_due -= payment
        if amount_due > 0:
            print(f"Amount Due: {amount_due}" )
        else:
            print(f"Change Owed: {-amount_due}")
            break

main()