f = open('Логи.jmx', 'r')

list = []

for line in f:
    s = line.split(',')
    list.append(s[3])

def frequency_sort(items):
    list1 = []
    for i in range(1, len(items)):
        if list1.count(items[i]) == 0:
            for a in range(0, items.count(items[i])):
                list1.append(items[i])
    dict = {}

    for i in range(0, len(list1)):
        a = list1[i]
        b = list1.count(list1[i])
        dict[a] = b

    return dict

print(frequency_sort(list))
