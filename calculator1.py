# 201504003 구본익
# 2019.03.28 자정까지!!
# Lab : 구구단 계산기
print("몇단을 출력하시겠습니까?")
user_input = input()
print("구구단", user_input, "단을 계산")
int_input = int(user_input) # int 형으로 변환하여 대입
for i in range(1,10): # 1부터 10까지 i로 차례대로 대입
    result = int_input * i
    print(user_input, " x ", i, " = ", result)