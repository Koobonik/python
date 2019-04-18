# 1. 값 받아서 계산 실수로 정의 해야함 (flaot)int 이런식으로 아마 하지않을까 섭씨 화씨 계산?? 소수점 어디까지 찍어줄지

# 섭씨 -> 화씨  = (섭씨 * 1.8) + 32

print("섭씨 온도를 입력해주세요.")
user_input = float(input())

hwa = user_input * 1.8 + 32
print("온도는 %.2f 입니다" % hwa)