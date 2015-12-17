digits = pow(2, 1000)
result = 0

print(digits)

while (digits != 0):
    result += digits % 10
    digits = digits // 10

print(result)
