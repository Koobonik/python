#  야구 게임 세자리중 중복숫자 안됨

import random
a = ''
while True:
    q = random.randint(1, 9)
    w = random.randint(1, 9)
    e = random.randint(1, 9)
    if q != w and w != e and q != e:
        a = str(q) + str(w) + str(e)
        break



print(a)
b = str(input("숫자를 입력하시오"))

strike = 0
ball = 0

for number in list(a):
    if b.count(number) >= 1:  # 같은게 있다면 1이상일 것임
        if b.find(number) == a.find(number):
            strike += 1
        else:
            ball += 1


print("Strike: ", strike, " Ball ", ball)