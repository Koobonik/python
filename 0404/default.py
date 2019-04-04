def print_something_2(my_name, your_name = "TEAMLAB"):
    print("Hello {0}, My name is {1}".format(your_name, my_name))


print_something_2("Sungchul", "TEAMLAB")
print_something_2("Sungchul")  # 하나만 넣어도 디폴드 값이 있어서 괜찮다.