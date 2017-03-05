# reading all names into list
namesFile = open("files/p022_names.txt")
namesString = namesFile.read().lower()
namesString = namesString.replace('"', "")
namesList = namesString.split(",")

namesList.sort()


result = 0
i = 1
for name in namesList:
    score = 0
    for c in name:
        score += ord(c) - 96
    score *= i
    result += score
    i += 1

print(result)
