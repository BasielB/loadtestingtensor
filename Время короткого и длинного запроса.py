import time

f = open('Логи.jmx', 'r')

timeList = []

dict = {}

for line in f:
    s = line.split(',')
    dict[s[1]] = s[0]
    timeList.append(s[1])


tmplist = []

for i in timeList:
    if i.isdigit() == True and int(i) > 1:
        tmplist.append(int(i))

tmplist.sort()

fastTime = tmplist[0]
longTime = tmplist[-1]

ft = dict.get(str(fastTime))[0:0-3]
lt = dict.get(str(longTime))[0:0-3]




print("Точное время самого быстрого запроса:", time.ctime(int(ft)))
print("Точное время самого длинного запроса:", time.ctime(int(lt)))





