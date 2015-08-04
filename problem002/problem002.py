fib1 = 1
fib2 = 2
adder = 0

while (fib1 < 4000000 and fib2 < 4000000):
    temp = fib2
    fib2 += fib1
    fib1 = temp
    if (fib1 % 2 == 0):
        adder += fib1
print(str(adder))
