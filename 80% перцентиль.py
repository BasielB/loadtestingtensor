import numpy as np

f = open('Логи.jmx', 'r')

timeList = []

for line in f:
    s = line.split(',')
    if s[1].isdigit() == True and int(s[1]) > 0:
        timeList.append(int(s[1]))

print(np.percentile(timeList, 80))


