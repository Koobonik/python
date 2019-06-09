result = [i if i % 2 == 0 else 10 for i in range(10)]
#  result[0] = ???
print(result)

for i in range(10):
    if i % 2 == 0:
        print(i)
    else:
        print(10)



