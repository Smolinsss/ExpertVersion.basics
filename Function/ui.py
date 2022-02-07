# user interface module

from os import system

def printClientCarMenu():
    print("#"*50)
    print("1. Show car list")
    print("2. Rent a car")
    print("3. Return a car")
    print("0. Exit")
    print("#"*50)

    option = int(input(">>> "))
    return option



def printAdminCarMenu():
    print("#"*50)
    print("1. Show car list")
    print("2. Show clients")
    print("3. Add a car")
    print("4. Edit a car")
    print("5. Delete a car")
    print("9. Logout")
    print("0. Exit")
    print("#"*50)

    option = int(input(">>> "))
    return option

def wait():
    input("Hit 'ENTER' to continue")


def clear():
    system("cls")


############### ADMIN ###############

def loginAdministrator():
    login = input("Admin login: ")
    passw = input("Admin password: ")
    if login == "admin" and passw == "123":
        return True
    else:
        return False




