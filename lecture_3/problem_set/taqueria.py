def main():
    # set up total_price variable as float.  
    total_price = 0.0
        
    while True:
        # try to take order, if EOFError or a Keyboard innterupt print total price and break loop
        try: 
            price = take_order()
        except (EOFError, KeyboardInterrupt):
            print(f"Total: ${total_price}")
            break
           
        # if price contains invalid input, print total, otherwise add price to total price. 
        if price == None:
            print(f"Total: ${total_price}")
        else:
            total_price += price
            print(f"Total: ${total_price}")
    
def take_order():
    menu = {
        "Baja Taco": 4.25,
        "Burrito": 7.50,
        "Bowl": 8.50,
        "Nachos": 11.00,
        "Quesadilla": 8.50,
        "Super Burrito": 8.50,
        "Super Quesadilla": 9.50,
        "Taco": 3.00,
        "Tortilla Salad": 8.00
        }
        
    # convert user input to lower case.  For case insensitive look up.
    item_ordered = input("Item: ").lower()
    
    # recreate menu dictionary with lower case keys.  Also for case insensitive look up.
    lowercase_dict = {key.lower(): value for key, value in menu.items()}
    
    # look up price by item inputed by user.
    menu_item_price = lowercase_dict.get(item_ordered)
    
    # return price of item
    return menu_item_price

main()