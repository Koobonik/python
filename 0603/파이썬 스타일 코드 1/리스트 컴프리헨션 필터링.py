case_1 = ["A", "B", "C"]
case_2 = ["D", "E", "A"]
result = [i + j for i in case_1 for j in case_2 if not(i == j)]
print(result)

result = [i + j for i in case_1 for j in case_2 if (i == j)]
print(result)



# 얘네는 중복이 있음
result2 = [[i + j for i in case_1] for j in case_2]
print(result2)


#  중복을 제거하려면?
result2 = [[i + j for i in case_1 if not (i == j)] for j in case_2]
print(result2)


# 중복만 표시하려면?
result2 = [[i + j for i in case_1 if(i == j)] for j in case_2]
print(result2)


result = [i + j for i in case_1 for j in case_2]
print(result)