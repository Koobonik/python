def test(t):
    print(x)
    t = 20
    print("In Function:", t)


x = 10
test(x)
print("In Main:", x)
print("In main:", t)  # t 라는 변수는 선언되어 있지 않으므로 출력 x
