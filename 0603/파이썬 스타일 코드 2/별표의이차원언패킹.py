a, b, c = ([1, 2], [3, 4], [5, 6])
print(a, b, c)


data = ([1, 2], [3, 4], [5, 6])
print(*data)


for i, v in enumerate(zip(*data)):
    print(i, v)