solution = 0

# 0=monday 1=tuesday 2=wednesday 3=thursday 4=friday 5=saturday 6=sunday
weekday = 1

for year in range(1901, 2001):

    # calculate february
    february = 28
    if (year % 4) == 0:
        if (year % 100) == 0:
            if (year % 400) == 0:
                february = 29
        else:
            february = 29

    months = [31, february, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

    for month in months:
        monthday = 0
        while monthday < month:
            if monthday == 0 and weekday == 6:
                solution += 1
            monthday += 1
            weekday = (weekday + 1) % 7

print solution
