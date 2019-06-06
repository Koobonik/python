def print_name_age_addr(name, age, addr):
    print(f"name : {name}")
    print(f"age : {age}")
    print(f"addr : {addr}")



my_dict = {
    'name': 'lee',
    'age': '30',
    'addr': 'seoul'
}
print_name_age_addr(**my_dict)
print_name_age_addr(my_dict['name'], my_dict['age'], my_dict['addr'])