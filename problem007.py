def is_prime(n):
    if n == 2 or n == 3:
        return True
    if n % 2 == 0:
        return False
    if n < 9:
        return True
    if n % 3 == 0:
        return False
    r = int(n ** 0.5)
    f = 5
    while f <= r:
        if n % f == 0:
            return False
        if n % (f + 2) == 0:
            return False
        f += 6
    return True

count = 2
prim = 0
while True:
    if is_prime(count):
       prim += 1
       if prim == 10001:
           break
    count += 1

print(str(count))
