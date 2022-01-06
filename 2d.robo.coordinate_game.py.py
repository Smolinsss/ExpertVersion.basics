from os import system
from random import randint

# a - move left
# d - move right
# w - move up
# s - move down
# x - exit

roboHP = 100
roboCHARGE = 100
coins = 0

roboX = 1
roboY = 1
bomb1X = 3
bomb1Y = 3
exitX = 8
exitY = 8
coinsX = 4
coinsY = 6

while True:
    system("cls")
    print("\nYou need to get to the exit!\nGood luck!\n")

    if roboX == exitX and roboY == exitY:
        coins += 150
        print("✌ ✌ ✌YOU WON!!!✌ ✌ ✌\nYour coins: " + str(coins))
        break

    if roboX == bomb1X and roboY == bomb1Y:
        roboHP -= 50  
        print("🔥🔥🔥 You hit a bomb 🔥🔥🔥\n🔥🔥🔥  - 50 health   🔥🔥🔥")
        bomb1X = "▪"
        bomb1Y = "▪"

    if roboX == coinsX and roboY == coinsY:
        coins += 30
        print("💲💲💲 You got the coins!!! 💲💲💲")
        coinsX = "▪"
        coinsY = "▪"

    if roboCHARGE <= 0 or roboHP <= 0:
        print("❌❌❌ GAME OVER ❌❌❌")
        break
    
    print("\n")
    print("Robot Health: " + str(roboHP))
    print("Robot Charge: " + str(roboCHARGE))
    print("Coins: " + str(coins))
    print("\n")
    for y in range(1,9):
        for x in range(1,9):
            if x == roboX and y == roboY:
                print("🤖", end="  ")
            elif x == bomb1X and y == bomb1Y:
                print("💣", end="  ")
            elif x == exitX and y == exitX:
                print("🚪 ", end=" ")
            elif x == coinsX and y == coinsY:
                print("💰", end="  ")
            else:
                print(" ▪ ", end=" ")
        print()

    direction = input("dir (a/d/w/s/x) >>> ")
    if direction == "a":
        roboX -= 1
        if roboX == 0:
            roboX = 8
        roboCHARGE -= 5
    if direction == "d":
        roboX += 1
        if roboX == 9:
            roboX = 1
        roboCHARGE -= 5
    if direction == "w":
        roboY -= 1
        if roboY == 0:
            roboY = 8
        roboCHARGE -= 5
    if direction == "s":
        roboY += 1
        if roboY == 9:
            roboY = 1
        roboCHARGE -= 5
    
    if direction == "x":
        system("cls")
        print("🤟🤟🤟 Thank you for playing!!! 🤟🤟🤟")
        break
