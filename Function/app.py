from car import *
from ui import *

is_admin = False

cars = [
    createCar("car_plate", "brand", "year", True, "price"),
    createCar("car_plate", "brand", "year", True, "price"),
    createCar("car_plate", "brand", "year", True, "price"),
    createCar("car_plate", "brand", "year", True, "price"),
    createCar("car_plate", "brand", "year", True, "price"),
    createCar("car_plate", "brand", "year", True, "price"),
    createCar("car_plate", "brand", "year", True, "price")
]

clients = []

def rentCar():

    id = input("Enter registration number: ")
    s = next(i for  i in cars if i["car_plate"] == id)   
    ind = cars.index(s)
    cars[ind]["rented"] = False 
    t = int(input("Specify the number of days: "))
    p = cars[ind]["price"] * t
    print("Car rental cost " + str(p) + "$")



    
def returnCar():
    id = input("Enter registration number: ") 
    s = next(i for  i in cars if i["car_plate"] == id)   
    ind = cars.index(s)
    cars[ind]["rented"] = True


while True:
    clear()

############# CLIENT ###################

    if not is_admin:
        option = printClientCarMenu()

        if option == 1:
            clear()
            printCarListInfo(cars)
            wait()

        if option == 2:
            clear()
            printCarListInfo(cars)
            rentCar()
            wait()
            
        if option == 3:
            clear()
            returnCar()
            print("Thanks for choosing us! Waiting for you more!")
            wait()
            
        if option == 0:
            break

            ####### ADMIN Login ###########
        if option == 9:
            is_admin = loginAdministrator()

############## ADMIN ####################
    else:
        option = printAdminCarMenu()

        if option == 1:
            clear()
            printCarListInfo(cars)
            wait()

        if option == 2:
            pass

        if option == 3:
            pass

        if option == 4:
            pass

        if option == 5:
            pass


        if option == 9:
            is_admin = False

        if option == 0:
            break
