shopping_cart = {}


print("Welcome to the Shopping Cart Program!")

def addItem():
    item = input("What item would you like to add? ")
    price = float(input(f"What is the price of '{item}'? "))
    shopping_cart[item] = round(price,2)
    print(f"{item} has been added to the cart.")

def printCart():
    print("The contents of the shopping cart are:")
    counter = 1
    for item, price in shopping_cart.items():
        print(f"{counter}. {item} - ${price}")
        counter+=1

def removeItem():
    selection = int(input("Which item would you like to remove? ")) - 1
    items = list(shopping_cart.keys())
    item = items[selection]
    shopping_cart.pop(item)

def computeTotal():
    values = shopping_cart.values()
    total = 0.00
    for value in values:
        total += value
    print(f"The total price of the items in the shopping cart is ${total}")

while True:
    direction = input(
        """
        Please select one of the following: /n
        1. Add item/n
        2. View cart/n
        3. Remove item/n
        4. Compute total/n
        5. Quit/n
        Please enter an action: """)
    match int(direction):
        case 1:
            addItem()
        case 2:
            printCart()
        case 3:
            removeItem()
        case 4:
            computeTotal()
        case 5:
            print("Thank you. Goodbye.")
            break
        case _:
            print("number not it range, please try again")
            continue