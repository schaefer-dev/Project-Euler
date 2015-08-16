x = 20
count = 0
while True:
    solution = True
    if (x % 1000000 == 0):
        count += 1
        print("step1000000 " + str(count))
    for i in range(1, 20, 1):
        if (solution):
            if (not (x % i == 0)):
                solution = False
                break

    if (solution):
        print("!!! SOLUTION !!! " + str(x))
    else:
        x += 1
