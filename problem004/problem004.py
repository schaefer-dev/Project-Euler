# A palindromic number reads the same both ways. The largest palindrome made
# from the product of two 2-digit numbers is 9009 = 91 x 99.
# Find the largest palindrome made from the product of two 3-digit numbers.

max = 999 * 999

x = 999
y = 999
finished = False
solutions = []

for x in range(999, 100, -1):
    if (not finished):
        for y in range(999, 100, -1):
            if (not finished):
                checkit = x * y
                if (checkit % 10) == (checkit / 100000):
                    if (((checkit % 100) / 10) == ((checkit / 10000) % 10)):
                        if (((checkit % 1000) / 100) == ((checkit / 1000) % 10)):
                            print("the solution is x:" + str(x) +"and y:" + str(y))
                            print("and their product is " + str(x * y))
                            solutions.append(x * y)

maxi = 0
for x in solutions:
    if (x > maxi):
        maxi = x

print("biggest number is: " + str(maxi))
print("Game over!")
