# If we list all the natural numbers below 10 that are multiples of 3 or 5,
# we get 3, 5, 6 and 9. The sum of these multiples is 23.bit_length

# Find the sum of all the multiples of 3 or 5 below 1000.bit_length

adder = 0
i = 0
for i in range(1000):
    if (i % 3 == 0):
        adder += i
    else:
        if (i % 5 == 0):
            adder += i
print(str(adder))
