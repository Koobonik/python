# 201504003 구본익
# 2019.03.28 자정까지!!
import random

guess_number = random.randint(1,100) # 1~100까지 정수형 난수 발생
print("숫자를 맞혀보세요.")

user_input = int(input())

# 사용자가 1 ~ 100사이의 숫자중 맞추지 못할경우 반복
while (user_input is not guess_number):
    if user_input > guess_number:
        print("숫자가 너무 큽니다")
    else:
        print("숫자가 너무 작습니다.")
    user_input = int(input())
# 정답일경우
else:
    print("정답입니다. 입력하신 숫자는 :", user_input," 입니다.")