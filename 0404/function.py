def f(x):
    return 2 * x + 7
def g(x):
    return x ** 2
x = 2
# f(x) == 11, g(x) == 4, f(g(x)) == 15, g(f(x)) == 121
print(f(x) + g(x) + f(g(x)) + g(f(x))) # 다 더한 151 출력