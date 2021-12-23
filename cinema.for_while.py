seats = [0, 0, 0, 0, 0]
while True:
    print(" 1", "2", "3", "4", "5", sep="  ")
    for n in seats:
        if n == 0:
            print("| |", end="")
        else:
            print("|x|", end="")
    print("\n---------------\n| | - free\n|x| - occupied")
    
    s = int(input("Pick a seate (1-5): ")) - 1
    if s in range(5):
        if seats[s] == 0:
            print("Yes,", s+1, " seat is free!")
            confirm = input("Buy(yes/no)?")
            if confirm == "yes":
                if (s+1 == 1) or (s+1 == 5):
                    print("You have to pay - 90 mdl.")
                elif (s+1 == 2) or (s+1 == 4):
                    print("You have to pay - 140 mdl.")
                else:
                    print("You have a VIP.\nYou have to pay - 200 mdl.")
                    
                seats[s] = 1     
        else:    
            print("No, sorry,", s+1, " seat is occupied")
               
    else:
        print("Wrong place chosen.\nTry again!")
