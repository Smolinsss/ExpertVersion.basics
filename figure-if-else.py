figure = input("What figure to draw: ")
if figure == "line":
    print("-----")
elif figure == "square":
    print("----- ", "|   |", "|   |", "----- ", sep="\n" )
elif figure == "parallel horizontal lines":
    print(" ----- ", " ----- ", sep="\n")
elif figure == "parallel vertical lines":
    print(" |    | ", " |    | ", sep="\n")
else:
    print("I can't draw such a picture!")