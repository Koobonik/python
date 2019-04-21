#  1 ~ 1000 까지의 3의 합을 구하여라

sum = 0
for i in range(1, 1000):
    if (i % 3) == 0:
        sum += i


print(sum)