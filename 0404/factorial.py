def factorial(n):
    if n == 1:
        return 1
    else:
        return n * factorial(n - 1)

#  5 넣으면 5 * 4 * 3 * 2 * 1 이 계산되어 120이 출력될 것임 
print(factorial(int(input("Input Number for Factorial Calculation: "))))