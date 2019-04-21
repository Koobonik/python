def maxx(sub):
    max = sub[0]
    for i in range(len(sub)):
        if (sub[i] > max):
            max=sub[i]
    return max

m = [55,70,43,88,99]
k = [88,78,67,54,98]
e = [50,86,64,67,37]

aver=[m,k,e]

print("수학 max : ", maxx(m))
print("국어 max : ", maxx(k))
print("영어 max : ", maxx(e))