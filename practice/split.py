# 문자열 나누기

pin = "960130-1123344"

hepp = pin.split("-")

print(hepp[0] + " and " + hepp[1])


we = "a:b:c:d"

re = we.replace(":", "#")


hong = {}
hong["국어"] = 80
hong["영어"] = 75
hong["수학"] = 55
sum = 0
for i in hong.values():
    sum += i


print(sum/3)