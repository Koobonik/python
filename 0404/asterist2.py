def asterisk_test(a, b, *args):
    print(args)
    print(args[0])
    # return 값이 없기에 밑에 print 에는 None 값이 출력 될 것이다.
    

print(asterisk_test(1, 2, 3, 4, 5))  # 튜플 자료형
