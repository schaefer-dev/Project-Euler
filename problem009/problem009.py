import math

a = 0
b = 0

for a in range(1, 1000, 1):
    for b in range(1, 1000, 1):
        c = math.sqrt(a * a + b * b)
        if (a + b + c == 1000):
            print(str(a * b * c))
            break
