print("십진수 입력해주세요")
decimal = int(input())
result = ''
while (decimal > 0):
    remainder = decimal % 2 # 나머지를 구하는곳
    decimal = decimal // 2 # 몫을 구하는 곳
    result = str(remainder) + result
print(result)

print( 1 % 2)

# 4 들어감
# 나머지 0
# 2
# result 에는 0 + ''
#

# 00