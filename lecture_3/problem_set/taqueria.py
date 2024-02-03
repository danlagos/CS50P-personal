def main():
    item = take_order()
    calculate_total(item)
    
def take_order():
    return input("Item: ")

def calculate_total(item):
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
    
    print(item)
    print(f"Price: {menu[item]}")

main()