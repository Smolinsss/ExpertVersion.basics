from os import system

tasks = []

while True:
    print("\n\tTODO App")
    choice = int(input("\nMenu\n1-add task\n2-show task\n3-remove task\n4-clear TODO\n0-exit\n"))
    system("cls")
    if choice == 1:
        new_task = input("Add task: ")
        system("cls")
        if new_task not in tasks:
            tasks.append(new_task)
        else:
            print("\nThis task already EXISTS!!!")
    elif choice == 2:
        print("TODO list (", len(tasks), "): ")
        for i in range(len(tasks)):
            print("\t", i+1, ">", tasks[i])
    elif choice == 3:
        if len(tasks):
            print("TODO list (", len(tasks), "): ")
            for i in range(len(tasks)):
                print("\t", i+1, ">", tasks[i])
            n = int(input("Which position are we deleting: "))
            tasks.pop(n-1)
        else:
            print("The list is empty\nThere is nothing to delete")   
    elif choice == 4:
        if len(tasks):
            tasks.clear()
            print("TODO list (", len(tasks), "): ")
        else:
            print("The list is empty\nThere is nothing to delete")
    else:
        if choice == 0:
            print("Goodbye!")
            break
        else:
            print("Not entered correctly!")


