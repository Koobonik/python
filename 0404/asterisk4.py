def asterisk_test_2(*args):
    x, y, *z = args
    return x, y, z


print(asterisk_test_2(3, 4, 5, 10, 20))  # 두번째 열 이후의 요소들은 배열로 들어갈 것임
