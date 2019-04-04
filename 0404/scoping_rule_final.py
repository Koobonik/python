def calculate(x, y):
    total = x + y
    print("In Function")
    #  5, 7, 12, 12 출력
    print("a:", str(a), "b:", str(b), "a + b:", str(a + b), "total:", str(total))
    return total


a = 5
b = 7
total = 0
print("In Program -1")
print("a:", str(a), "b:", str(b), "a + b:", str(a + b))  # 5 + 7 = 12

sum = calculate(a, b)
print("After Calculation")
print("Total:", str(total), "Sum:", str(sum))  # 0 출력 12 출력
