# 201504003 구본익
# 2019.03.28 자정까지!!

print("몇단?")
user_input = input()
print("구구단", user_input, "단을 계산")
int_input = int(user_input)
for i in range(1,10):
    result = int_input * i
    print(user_input, " x ", i, " = ", result)