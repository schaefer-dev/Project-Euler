def factorial( x ):
    if x == 1:
        return 1
    else:
        return x * factorial(x-1)

solution = 0

x = int(input("value of x to compute x!"))

number = factorial(x)

while number > 0:
    solution += number % 10
    number = number // 10

print solution
