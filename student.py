# 201504003 구본익
# 2019.03.28 자정까지!!
print("당신이 태어난 연도를 입력하세요")
birth_year = input()
age = 2020 - int(birth_year) + 1

if age <= 26 and age >= 20 :
    print("대학생")
elif age < 20 and age >= 17 :
    print("고등학생")
elif age < 17 and age >= 14 :
    print("중학생")
elif age < 14 and age >= 8 :
    print("초등학생")
else:
    print("학생이 아닙니다.")