def print_customer_info(**kwargs):
    for key in kwargs:
        print(f"{key}: {kwargs[key]}")


print_customer_info(name="lee", age="30")
print_customer_info(name="lee", age="30", address="seoul")
