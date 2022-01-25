def wrapBrackets(text):
    return "(" + text + ")"

def wrapPackaging(text1):
    return "[[[" + text1 + "]]]"

def wrapPacker(text2):
    return "<<<" + text2 + ">>>"


a = wrapBrackets("12345")
b = wrapPackaging(a)
print(wrapPacker(b))




