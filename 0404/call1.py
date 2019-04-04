def f(x):
    y = x
    x = 5
    return y * y

x = 3
print(f(x)) # 9 출력
print(x) # 3 출력