ex = [1, 2, 3, 4, 5]
f = lambda x, y: x + y
print(list(map(f, ex ,ex)))


#  다른 방법으로도 가능하다
#  리스트 컴프리헨션
print([x + y for x, y in zip(ex, ex)])


