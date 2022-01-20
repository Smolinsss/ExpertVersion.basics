from os import system
from time import sleep



room_map = [
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 1, 1, 1, 1, 1, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 3, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
]

robo_steps = [
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
]

dust_map = [
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 1, 1, 0, 0, 1, 1, 0, 0, 0],
    [0, 1, 0, 1, 0, 0, 0, 1, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 1, 0, 0],
    [0, 1, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 1, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 1, 0, 1, 0, 0, 1, 0, 0],
    [0, 0, 1, 0, 0, 0, 1, 1, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
]

charge = 100
score = 0
robo_x = 8
robo_y = 8
robo_steps[robo_x][robo_y] = 1

n = 0
for i in range(len(dust_map[1])):
    for y in range(len(dust_map)):
        if dust_map[i][y] == 1:
            n += 1



while True:
   
    system("cls")
    print("Charge status " + str(charge))
    print("It was removed " + str(score) + " square meters")
    print("It remains to remove " + str(n) + " square meters\n")

    for x in range(len(room_map[1])):
        for y in range(len(room_map)):
            if robo_x == x and robo_y == y:
                print("R", end=" ")
            elif room_map[x][y] == 0:
                print(".", end=" ")
            elif room_map[x][y] == 1:
                print("#", end=" ")
            elif room_map[x][y] == 3:
                print("B", end=" ")  
        print(" |", x+1, end="")  
        print()
    print("-"*19)

    for y in range(len(room_map)):
        print(y+1, end=" ")
    print()


    print("\n")

    for x in range(len(robo_steps[1])):
        for y in range(len(robo_steps)):
            if robo_steps[x][y] == 0:
                print(".", end=" ")
            elif robo_steps[x][y] == 1:
                print("+", end=" ")
        print(" |", x+1, end="")  
        print()
    print("-"*19)

    for y in range(len(room_map)):
        print(y+1, end=" ")
    print()
    
    print("\n")

    for x in range(len(dust_map[1])):
        for y in range(len(dust_map)):
            if dust_map[x][y] == 0:
                print(".", end=" ")
            elif dust_map[x][y] == 1:
                print("@", end=" ")
        print(" |", x+1, end="")  
        print()
    print("-"*19)

    for y in range(len(room_map)):
        print(y+1, end=" ")
    print() 


    if robo_x > 0 and room_map[robo_x - 1][robo_y] != 1 and robo_steps[robo_x - 1][robo_y] != 1:
        robo_x -= 1
        charge -= .1
    elif robo_y < 9 and room_map[robo_x][robo_y + 1] != 1 and robo_steps[robo_x ][robo_y + 1] != 1 :
        robo_y += 1
        charge -= .1   
    elif robo_x < 9 and room_map[robo_x + 1][robo_y] != 1 and robo_steps[robo_x + 1][robo_y] != 1:
        robo_x += 1 
        charge -= .1   
    elif robo_y > 0 and room_map[robo_x][robo_y - 1] != 1 and robo_steps[robo_x][robo_y - 1] != 1:
        robo_y -= 1
        charge -= .1

    elif robo_x > 0 and room_map[robo_x - 1][robo_y] != 1 and robo_steps[robo_x - 2][robo_y] != 1:
        robo_x -= 1
        charge -= .1
    elif robo_y < 9 and room_map[robo_x][robo_y + 1] != 1 and robo_steps[robo_x ][robo_y + 2] != 1 :
        robo_y += 1
        charge -= .1   
    elif robo_x < 9 and room_map[robo_x + 1][robo_y] != 1 and robo_steps[robo_x + 2][robo_y] != 1:
        robo_x += 1 
        charge -= .1   
    elif robo_y > 0 and room_map[robo_x][robo_y - 1] != 1 and robo_steps[robo_x][robo_y - 2] != 1:
        robo_y -= 1
        charge -= .1

    elif robo_x > 0 and room_map[robo_x - 1][robo_y] != 1 and robo_steps[robo_x - 3][robo_y] != 1:
        robo_x -= 1
        charge -= .1
    elif robo_y < 9 and room_map[robo_x][robo_y + 1] != 1 and robo_steps[robo_x ][robo_y + 3] != 1 :
        robo_y += 1
        charge -= .1   
    elif robo_x < 9 and room_map[robo_x + 1][robo_y] != 1 and robo_steps[robo_x + 3][robo_y] != 1:
        robo_x += 1 
        charge -= .1   
    elif robo_y > 0 and room_map[robo_x][robo_y - 1] != 1 and robo_steps[robo_x][robo_y - 3] != 1:
        robo_y -= 1
        charge -= .1


    if dust_map[robo_x][robo_y] == 1:
            score += 1
            n -= 1
            charge -= 1
    if charge < 2:
        print("\nLow battery charge!")
        break
    

    robo_steps[robo_x][robo_y] = 1
    dust_map[robo_x][robo_y] = 0
    sleep(0.3)
