def getMax(array):
    max = array[0]
    print(len(array))
    for i in range(len(array)):
        if max < array[i]:
            max = array[i]

    return max



m = [55,70,43,88,99]  # 수학
k = [88,78,67,54,98]  # 국어
e = [50,86,64,67,37]  # 영어

print("수학 max ", getMax(m))
print("국어 max ", getMax(k))
print("영어 max ", getMax(e))