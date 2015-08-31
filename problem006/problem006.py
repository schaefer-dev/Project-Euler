sum1 = 0
for i in range(1, 100, 1):
    sum1 += i * i

sum2 = 0
for i in range(1, 100, 1):
    sum2 += i
sum2 = sum2 * sum2

print(str(sum2-sum1))
