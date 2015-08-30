nextadd = 1
triangle = 0

progress = 0
stepstone = 0


def extraTest(value):
    if (value % 4 != 0):
        return False
    if (value % 3 != 0):
        return False
    return True


while(True):
    triangle += nextadd
    nextadd += 1
    progress += 1
    if (progress % 100 == 0):
        stepstone += 1
        print('step: ' + str(stepstone) + '00 with triangle: ' + str(triangle))

    teiler = 2
    teilercount = 1

    while((teiler + (498 - teilercount) <= (triangle / 2)) and (teilercount != 500)):
        if (not(extraTest(triangle))):
            break
        if (triangle % teiler == 0):
            teilercount += 1
        teiler += 1

    if teilercount == 500 :
        print(triangle)
        exit

