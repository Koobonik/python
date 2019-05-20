u = [1, 2, 3]
v = [4, 4, 4]
alpha = 2

result = [alpha * sum(t) for t in zip(u, v)]
print(result)