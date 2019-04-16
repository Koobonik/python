import collections

deq = collections.deque(['a', 'b', 'c', 'd', 'e'])
deq.rotate(1)  # 한 번 오른쪽으로 이동
print('deq >>', ' '.join(deq))  # 한 칸 띄어서 조인

deq2 = collections.deque(['a', 'b', 'c', 'd', 'e'])
deq2.rotate(2)
print('deq2 >>', ' '.join(deq2))

deq3 = collections.deque(['a', 'b', 'c', 'd', 'e'])
deq.rotate(-1)
print('deq >>', ' '.join(deq))

deq4 = collections.deque(['a', 'b', 'c', 'd', 'e'])
deq4.rotate(-2)
print('deq4 >>', ' '.join(deq4))

