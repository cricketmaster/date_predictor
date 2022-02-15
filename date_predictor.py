import math

days = ["monday","tuesday","wednesday","thursday","friday","saturday","sunday"]
pattern = ["tuesday","sunday","friday","wednesday"]
daysinamonth = [31,[28,29],0,31,61,92,122,153,184,214,245,275]

date = input("date: ")
date = date.split("/")
for i in range(3):
    date[i] = int(date[i])

century = math.floor(date[2]/100)
century = pattern[century % 4]
for i in range(len(days)):
    if century == days[i]:
        start = i

difference = date[2] - (math.floor(date[2]/100)*100)
piday = (start + difference + (difference//4)) % 7
day = piday


if date[1] > 3:
    day += daysinamonth[date[1]-1]
    day += date[0]
    day = day % 7
    print(days[day])
else:
    leap = False
    if date[2] % 4 == 0 and not(date[2] % 100 == 0):
        leap = True
    elif date[2] % 400 == 0:
        leap = True

    day = piday + 4
    if leap:
        day -= 1
    day = day % 7

    if date[1] == 2:
        day += 31
    day += date[0]
    day = day % 7
    print(days[day])

