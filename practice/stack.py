word = input("input")
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
print(a.keys())

for i in a.keys():
    print(i)
print(a['name'])
print(list( a.keys()))