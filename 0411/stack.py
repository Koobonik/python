word = input("Input a word: ")
world_list = list(word)
print(world_list)

result = []
for _ in range(len(world_list)):
    result.append(world_list.pop())  # result에 끝에다가 world_list의 맨 끝부터 하나씩 추가


print(result)
print(word[::-1])
