food_1_name = "Pizza"
food_2_name = "French fries"
drink_1_name = "CocaCola"
food_1_price = 100
food_2_price = 50
drink_1_price = 30
food_1_available = 5
food_2_available = 12
drink_1_available = 25

food_1_quantity = int(input("How many " + food_1_name + " do you want?"))
if 0 <= food_1_quantity <= food_1_available:
    food_1_cost = food_1_quantity * food_1_price
    print("You have ordered", food_1_quantity, "x", food_1_name, "=", food_1_cost)
else:
    print("Sorry, we don't have that many", food_1_name, "!"
          "We have", food_1_available, food_1_name, "!")
    food_quantity = int(input("How many " + food_1_name + " do you want?" ))
    food_1_cost = food_quantity * food_1_price
    print("You have ordered ", food_quantity, " x ", food_1_name, " = ", food_1_cost)
    
food_2_quantity = int(input("How many " + food_2_name + " do you want?"))
if 0 <= food_2_quantity <= food_2_available:
    food_2_cost = food_2_quantity * food_2_price
    print("You have ordered", food_2_quantity, "x", food_2_name, "=", food_2_cost)
else:
    print("Sorry, we don't have that many ", food_2_name, "!"
          "We have", food_2_available, food_2_name, "!")
    food_quantity_2 = int(input("How many " + food_2_name + " do you want?"))
    food_2_cost = food_quantity_2 * food_2_price
    print("You have ordered ", food_quantity_2, " x ", food_2_name, " = ", food_2_cost)
    
drink_1_quantity = int(input("How many " + drink_1_name + " do you want?"))
if 0 <= drink_1_quantity <= drink_1_available:
    drink_1_cost = drink_1_quantity * drink_1_price
    print("You have ordered", drink_1_quantity, "x", food_2_name, "=", drink_1_cost)
else:
    print("Sorry, we don't have that many ", drink_1_name, "!"
          "We have", drink_1_available, drink_1_name, "!")
    drink_1_quantity = int(input("How many " + drink_1_name + " do you want?"))
    drink_1_cost = drink_1_quantity * drink_1_price
    print("You have ordered ", drink_1_quantity, " x ", drink_1_name, " = ", drink_1_cost)
    
total_1 = food_1_cost + food_2_cost + drink_1_cost
print("Order price =", total_1)
del_1 = input("Do you need delivery(YES/NO):")
if del_1 == "YES":
    if total_1 > 1000:
        print("Your cost including delivery is", total_1, "Thank you!")
    else:
        del_price = total_1 + 150
        print("Your amount does not exceed 1000. You will have to pay for delivery 150."
              "Total amount with delivery =", del_price)
else:
    print("Thanks for your order! You can pick it up at our restaurant!")