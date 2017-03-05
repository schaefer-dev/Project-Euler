# naive approach calculating divisors
def d(x):
    result = 0
    for i in range(1, (x // 2) + 1):
        if x % i == 0:
            result += i
    return result

divisorsums = [0]
for i in range(1, 10000):
    divisorsums.append(d(i))

print divisorsums

solution = 0
for i in range(1, 10000):
    x = divisorsums[i]
    if x <= 9999 and x != i:
        y = divisorsums[x]
        if y == i:
            solution += y

print solution
