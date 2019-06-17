f = open("ex.txt", 'r')
he = list()
while True:
    line = f.readline()
    if not line:break
    he.append(line)



f.close()
print(he)

for i, j in enumerate(he):
    print(i, j)


f = open("ex.txt", 'r')
lines = f.readlines()
for l in lines:
    print(l)


f.close()


#  r은 읽기전용 w는 다 지우고 다시 씀 거의 덮어쓰기? a 는 기존에서 추가 헤줌

