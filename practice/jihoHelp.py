#  50점 이상의 총합을 구하기
A = [20, 55, 67, 82, 45, 33, 90, 87, 100, 25]
sum = 0
#  for i in range(A.__len__()):
for i in range(len(A)):
    if A[i] >= 50:
        sum += A[i]


print(sum)
print(106)

a = 3.5
b = int(3.5)
print(a**(1) * 2)