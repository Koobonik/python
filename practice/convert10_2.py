#  이진수 변환 프로그램

int_input = int(input("숫자를 입력해주세요"))
result = ""
while int_input > 0:
    rem = int_input % 2  # 입력값의 2를 나누고 난 나머지 값을 넣어줌
    int_input = int_input // 2  # 그리고 몫을 넣어줌
    result = str(rem) + result  # 맨 앞자리부터 쌓여야 하므로 rem 이 앞으로간다


print(result)