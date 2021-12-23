from os import system
from random import randint

WATER = 0   # ◻
SHIP = 1    # ◼
MISS = 2    # ◦
HIT = 3     # ✖

Score = 0

colA = [0,     # 0
        0,     # 1
        0,     # 2
        0,     # 3
        0,     # 4
        0,     # 5
        0,     # 6
        0,     # 7
        0,     # 8 
        0      # 9
]
for i in range(3):
    colA[randint(0,9)]  = SHIP

counter = 0
while True:
    system("cls")
    print("Score: ", Score)

    for y in range(1,11):

        if colA[y-1] == WATER or colA[y-1] == SHIP:
            sign = "◻"
        if colA[y-1] == MISS:
            sign = "◦"
        if colA[y-1] == HIT:
            sign = "✖"

        print(sign, y)
        
    ShootY = int(input("shoot: "))
    
    if counter == 5:
        break
    counter += 1

    if colA[ShootY - 1] == SHIP:
        Score += 1
    if colA[ShootY - 1] == WATER:
        colA[ShootY - 1] = MISS
    if colA[ShootY - 1] == SHIP:
        colA[ShootY - 1] = HIT


print(" You've run out of moves\n Your score: ", Score)
       
        


