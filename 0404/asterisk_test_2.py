def asterisk_test_2(*args):
    x, y, *z = args
    return x, y, z


print(asterisk_test_2(3, 4, 5))  # 4 이후의 변수는 튜플 값으로 들어갈 것임
