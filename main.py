list = [4, 29, 1, 5, 11, 2, 7]
size = len(list) - 1

for x in range(size):
    for y in range(size - x):
        if list[y] > list[y + 1]:
            aux = list[y]
            list[y] = list[y + 1]
            list[y + 1] = aux

print(list)