file = open('numbers.txt','r')
numbers = []
for i in range(0,100):
    numbers.append(int(file.readline()))
print(sum(numbers))


# effektiv:
const = 100000000000000000000000000000000000000000
file = open('numbers.txt','r')
numbers = []
for i in range(0,100):
    numbers.append(int(file.readline()) / const)
print(sum(numbers))
