word = "input"
word_list = list(word)
print(word_list)

result = []

for i in range(len(word_list)):
    result.append(word_list.pop())


print(result)
print(word[::-1])

# () -> 튜플
# [] -> 리스트, 배열
# {} -> 딕셔너리, 집

s1 = set([1,2,3,4,5])
s2 = set([4,5,6,7,8])
print(s1 & s2)
print(s1 - s2)
a = {'name': 'pey', 'phone': '01022223333', 'birth': '1118'}
b = dict()
c = {}
print(a.keys())

for i in a.keys():
    print(i)
print(a['name'])
print(list(a.keys()))

print(list(a.items()))
print(type(a), type(b), type(c))

from collections import deque  # deque 쓰겠다고 선언
from collections import OrderedDict
from collections import defaultdict
deque_list = deque(s1)  # deque 로 초기화
print(s1.pop())  # deque 를 쓰지 않았으므로 앞에서부터 추출
print(s1.pop())
print(deque_list.pop())  # 얘는 deque 썼으니 뒤에서부터 뽑힘
deque_list.appendleft(6)  # 맨 앞에 6 추가
print(deque_list.popleft())  # 맨 앞꺼 추출

deque_list.rotate(2)
print(deque_list)
