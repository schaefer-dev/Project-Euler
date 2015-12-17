from num2words import num2words

stringlist = ''

for i in range(1,1001):
    stringlist += num2words(i)

stringlist = stringlist.replace('-','')
stringlist = stringlist.replace(' ','')

print(stringlist)
print(len(stringlist))
