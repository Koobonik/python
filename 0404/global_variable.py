def f():
    global s
    s = "I love London!"
    print(s)


s = "I love Paris!"  # 파리가 좋다고 저장되지만
f()  # f 함수에서 런던으로 바뀜
print(s) # 결국 런던 두번 출력
