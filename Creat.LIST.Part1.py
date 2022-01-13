clientsHighPriority = ["Tob", "Pete"]
clientsLowPriority = ["Vicky", "Lessly"]
clients = ["John", "Marry", "Kate"]
n = 0
for i in clientsHighPriority:
    clients.insert(n, i)
    n+=1
for i in clientsLowPriority:
    clients.append(i)
for el in range(len(clients)):
    print(el+1, clients[el])