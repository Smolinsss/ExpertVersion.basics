# CAR Module
from random import randint
from faker import Faker
from faker_vehicle import VehicleProvider

fake = Faker()
fake.add_provider(VehicleProvider)


def createCar(car_plate, brand, year, rented, price):
    
    car = {}
    car_plate = fake.license_plate()
    brand = fake.vehicle_make_model()
    year = fake.vehicle_year()
    price = randint(50, 120)
    car["car_plate"] = car_plate
    car["brand"] = brand
    car["year"] = year
    car["rented"] = bool(rented)
    car["price"] = price
    return car

def printCarInfo(car):
    print("-" * 100)
    print(f"# {car['car_plate']} / {car['brand']} / {car['year']} | Availability: {car['rented']} | {car['price']} $ per day")
    print("-" * 100)

def printCarListInfo(cars):
    for c in cars:
        printCarInfo(c)

