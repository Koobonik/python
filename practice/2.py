# 2. 간단하게 계산하는 문제? 조건은 함수를 def 함수 써서 그 함수 불러와서 계산
# 제곱을 반환하라

def getSum(x, y):
    sum = x + y
    return sum


def getZegob(x):
    zegob = x ** 2
    return zegob


print(getSum(3, 5))

print("제곱은 ", getZegob(5), "입니다.")