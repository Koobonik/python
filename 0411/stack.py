word = input("Input a word: ")  # hello world 를 입력
world_list = list(word)  # list로 변환
print(world_list)  # 각 요소마다 출력

result = []  # 뒤집을 때 저장될 변수
for _ in range(len(world_list)):  # 길이만큼 그리고 그 범위만큼 반복
    result.append(world_list.pop())  # result에 끝에다가 world_list의 맨 끝부터 하나씩 추가 world_list에는 마지막에 값이 더이상 없을것임


print(result)  # 뒤집힌글자가 들어감  
print(word[::-1])  # word를 뒤에서부터 출력
