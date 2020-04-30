
filein = open('input.txt', 'r', encoding='utf-8-sig')
fileout = open('output.txt', 'w', encoding='utf- 8')
alist = []
for line in filein:
    lists = list(map(str, line.split()))
    lists.remove(lists[2])
    alist.append(" ".join(lists))
alist.sort()
for i in range(0, len(alist)):
    print(alist[i], end='\n')
