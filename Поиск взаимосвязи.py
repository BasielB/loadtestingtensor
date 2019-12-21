import numpy as np

f = open('Логи последнего запроса.jmx', 'r')

listTime = []
listBytes = []

for line in f:
    s = line.split(',')
    s[-1] = s[-1][0:-1]
    if s[-1].isdigit() == True:
        if int(s[-1]) != 0:
            listTime.append(int(s[-1]))
            listBytes.append(int(s[-6]))

#print(listBytes)
#print(listTime)

print(np.corrcoef(listBytes, listTime)[0, 1])

