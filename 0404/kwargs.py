def kwargs_test(**kwargs):
    print(kwargs)
    print("First value is {first}".format(**kwargs))
    print("Second value is {second}".format(**kwargs))
    print("Third value is {third}".format(**kwargs))


kwargs_test(first=3, second=4, third=5)  # 딕셔너리 자료형
