def print_something(my_name, your_name):
    print("Hello {0}, My name is {1}".format(your_name, my_name))


print_something("Sungchul", "TEAMLAB")  # 내 이름과 너의 이름 순서대로 그냥 대입
print_something(your_name = "TEAMLAB", my_name = "Sungchul")  # 따로 지정도 가능하다.