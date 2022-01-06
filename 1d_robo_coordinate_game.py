from os import system

# a - move left
# d - move right
# x - exit

length = 30
roboHP = 100
roboCHARGE = 100
coins = 0
hearts1 = 10
roboX = 15
bombX1 = 12
bombX2 = 24
coins1 = 13
exit = 3

while True:
    system("cls")

    if roboX == exit:
        coins += 150
        print("✌ ✌ ✌YOU WON!!!✌ ✌ ✌\nYour coins: " + str(coins))
        break

    if roboX == hearts1:
        roboHP += 20
        print("💖💖 YOU GOT HEALTH 💖💖\n💖💖  + 20 health   💖💖")
        hearts1 = "▬"
        
        
    if roboX == coins1:
        coins += 35
        print("💲💲💲 You got the coins!!! 💲💲💲")
        coins1 = "▬"
        
    if roboX == bombX1 or roboX == bombX2:
        roboHP -= 50  
        print("🔥🔥🔥 You hit a bomb 🔥🔥🔥\n🔥🔥🔥  - 50 health   🔥🔥🔥")
        if roboX == bombX1:
            bombX1 = "▬"
        else:
            bombX2 = "▬"
        
        
        

    print("\nYou need to get to the exit!\nGood luck!\n")
    print("Robot Health: " + str(roboHP))
    print("Robot Charge: " + str(roboCHARGE))
    print("Coins: " + str(coins))
    if roboHP <= 0 or roboCHARGE <= 0:
        print("❌❌❌ GAME OVER ❌❌❌")
        break

    # ############## DRAWING THE MAP #############
    print("\n")
    x = 1  
    while x <= length:
        if x == roboX:
            print("🤖", end=" ")
        elif x == bombX1 or x == bombX2:
            print("💣", end=" ")
        elif x == hearts1:
            print("💙", end=" ")
        elif x == coins1:
            print("💰", end=" ")
        elif x == exit:
            print("🚪", end=" ")
        else:
            print("▬", end=" ")
        x += 1
            
    print("\n")

    # #############################################


    direction = input("dir (a/d/x) >>> ")

    if direction == "a":
        roboX -= 1
        if roboX == 0:
            roboX = 30
        roboCHARGE -= 5
    if direction == "d":
        roboX += 1
        if roboX == 31:
            roboX = 1
        roboCHARGE -= 5
    if direction == "x":
        system("cls")
        print("🤟🤟🤟 Thank you for playing!!! 🤟🤟🤟")
        break
   