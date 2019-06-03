case_1 = ["A", "B", "C"]
case_2 = ["D", "E", "A"]
result = [i + j for i in case_1 for j in case_2 if not(i == j)]
print(result)

result2 = [[i + j for i in case_1] for j in case_2]
print(result2)