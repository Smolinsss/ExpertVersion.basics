data1 = [-5, 0, 5, 10, -10, 15, -20, -35]
data2 = (-10, -1, 4, 15, -34, 15, -244, -36)
data3 = {-55, 5, 54, 103, -1034, 153, -204, -365}
data4 = True

def selectNegative(vector):
    if type(vector) != list and type(vector) != tuple and type(vector) != set:
        print("ERROR")
        return
    neg_vector = []
    for v in vector:
        if v < 0:
            neg_vector.append(v)
    return neg_vector

print(selectNegative(data1))
print(selectNegative(data2))
print(selectNegative(data3))
print(selectNegative(data4))
