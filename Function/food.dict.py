import os

menu = [
    {
        "name" : "Pizza",
        "price" : {
            "value" : 100.00,
            "unit" : "MDL"
        }
    },
    {
        "name" : "Salad",
        "price" : {
            "value" : 50.00,
            "unit" : "MDL"
        }
    }
]

def showMenu():
    print("\n")
    print("Menu.\n")
    for i in range(len(menu)):
        print(i+1, f'{menu[i]["name"]:2} {menu[i]["price"]["value"]:5} {menu[i]["price"]["unit"]:5}')
    

def makeOrder():

    name = input("What will you order: ")
    if name == "Pizza":
        quantity = int(input("How many: "))
        s = menu[0]["price"]["value"] * quantity
        print("\nFinal amount " + str(s), menu[0]["price"]["unit"])
    elif name == "Salad":
        quantity = int(input("How many: "))
        s = menu[1]["price"]["value"] * quantity
        print("\nFinal amount " + str(s), menu[1]["price"]["unit"])


def printMenu():
    print("1. Show menu.")
    print("2. Make an order.")
    print("3. Exit.")
    choise = int(input(">>> "))
    return choise


while True:
    os.system("cls")
    choise = printMenu()

    if choise == 1:
        showMenu()
        input("\nHit 'ENTER' to continue")

    elif choise == 2:
        makeOrder()
        input("\nHit 'ENTER' to continue")

    elif choise == 3:
        break
