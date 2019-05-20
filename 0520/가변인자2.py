my_info = ["lee", "30", "seoul", "010", "xxxx", "yyyy"]
name, age, address, *unknowns = my_info

print(name)
print(age)
print(address)
print(unknowns)


my_info = ["lee", "30", "seoul"]
name, age, address, *_ = my_info

