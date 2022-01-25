def drawLine(lenght, direction):
    if direction == "h":
        print("-" * lenght)
    elif direction == "v":
        for i in range(lenght):
            print("|")

drawLine(5, "h")
drawLine(3, "v")  