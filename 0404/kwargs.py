def kwargs_test(**kwargs):
    print(kwargs)
    #  밑에 변수들에 각 값들이 들어간다.
    print("First value is {first}".format(**kwargs))
    print("Second value is {second}".format(**kwargs))
    print("Third value is {third}".format(**kwargs))


kwargs_test(first=3, second=4, third=5)  # 딕셔너리 자료형
