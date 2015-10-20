start = 13
end = 1000000
amount = [0] * 1000001
startcount = start

while(startcount <= end):
    current = startcount
    while(current != 1):
        if (current % 2 == 1):
            # falls ungerade
            current = 3 * current + 1
            amount[startcount] += 1
        else:
            # falls gerade
            current = current / 2
            amount[startcount] += 1
    amount[startcount] += 1
    startcount+= 1

maxi = 0
result = 0
i = 0
while(i <= end):
    if(amount[i] > maxi):
        maxi = amount[i]
        result = i
    i += 1

print(result)



