# What is the largest prime factor of the number 600851475143 ?


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


for i in range(2, 600851475143, +1):
    if (600851475143 % i == 0):
        x = 600851475143 / i
        if (is_prime(x)):
            print(x)
            break
