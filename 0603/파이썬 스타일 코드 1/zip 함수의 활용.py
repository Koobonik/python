a, b, c = ((1, 2, 3), (10, 20, 30), (100, 200, 300))
print(a, b, c)
result = [sum(x) for x in zip(a, b, c)]
print(result)

alist = ['a1', 'a2', 'a3']
blist = ['b1', 'b2', 'b3']
for i, (a, b) in enumerate(zip(alist, blist)):
    print(i, a, b)


# for i, (a1,b1) in enumerate(zip(alist,blist)):
#     print(i, a1, b1)


for a, (i, j) in enumerate(zip("뻐킹1","뻐킹2")):
    print(a, b, c)




for i, j in enumerate(["본익이", "멍청함", "ㄹㅇ"]):
    print(i, j)