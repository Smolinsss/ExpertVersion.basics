from os import system

room_map = [
    [1, 1, 1, 1, 0, 0, 1, 1, 1, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 2, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 3, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
]

system("cls")

for x in range(len(room_map[1])):
    for y in range(len(room_map)):
        if room_map[x][y] == 0:
            print(".", end=" ")
        elif room_map[x][y] == 1:
            print("#", end=" ")
        elif room_map[x][y] == 2:
            print("R", end=" ")
        elif room_map[x][y] == 3:
            print("B", end=" ")
    print(" |", x+1, end="")  
    print()
print("-"*19)

for y in range(len(room_map)):
    print(y+1, end=" ")
