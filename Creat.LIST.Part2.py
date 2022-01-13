from os import system

clients = []
n = 0
while True:
    
    menu = int(input("\n 1 - Add VIP client\n 2 - Add Simple client\n 3 - Show clients\n 4 - Exit\n >>> "))
    system("cls")
    if menu == 1:
        vip_name = input("Enter the 'VIP' client's name: ").split()
        clients.insert(n, vip_name[0])
        n+=1
    if menu == 2:
        simple_name = input("Enter the 'Simple' client's name: ").split()
        clients.append(simple_name[0])
    if menu == 3:
        if len(clients) == 0:
            print("The list is empty")
        for el in range(len(clients)):
            print(el+1, clients[el])
    if menu == 4:
        break
        