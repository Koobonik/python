
#  세문자 클래스 세문제중 하나는 안배운거
#  #. 사용자가 잘못입력했을경우 잘 못입력했다고 말해주고 다시 입력하게 해줘야함 클래스를 사용하면
#  1. 랜덤함수를 쓸 줄 알아야함 조건 3개임 조건3개 만족해야 만점 30
#  2. 클래스를 만들고 숫자를이용하여 리스트컴프리헨션!을 쓸 수 있는지 없는지! 만약(if) 사용자가 어떤 문자를 입력했을때 종료하거나 계속하거나 30
#  3. 클래스를 만들고 그 클래스를 이용해서 ! 상속 ! 받아야함 그러면서~ 내부에 있는 메소드를 오버라이딩 하는 방법을 추가했음 40
#  실행파일은 실행하는 족족 캡처해서 첨부할것
import random

while True:
    try:
        print(random.randint(0, 2))
        user_input = (int(input('숫자를 입력해주세요')))

    except(ZeroDivisionError, ValueError):
        print('숫자만 입력하라니까?')

