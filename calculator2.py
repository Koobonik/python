# 201504003 구본익
# 2019.03.28 자정까지!!

x = 1
while (x is not 0):
    print("몇단?")
    x = int(input())
    if x is 0:
        break

    if not(1 <= x <= 9):
        print("잘못입력하셨습니다.")
        continue
    else:
        print("구구단", x, "단을 계산")
        x = int(x)
        for i in range(1, 10):
            result = x * i
            print(x, " x ", i, " = ", result)
        print("다른 계산을 하시겠습니까?")
print("구구단 계산을 종료합니다.")

