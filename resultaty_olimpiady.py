n = int(input())
alist = []
for i in range(0, n):
    name = list(input().split())
    alist.append(name)
#for i in range(0, len(alist)):
#    bal = alist[i][1]
#    name = alist[i][0]
#    alist.replace(name, bal)
#    alist.replace(bal, name)
#sort.alist(key=reverse)
#for i in range(0, len(alist)):
#    alist.remove(alist[i][0])
newList = []
for i in range(0, len(alist)):
    name = alist[i]
    listt = list(name)
    newList.append(listt)
#for i in range(0, len(alist)):
#    new0 = newList[i][0]
#    newList[i].replace(newList[i][0], newList[i][1])
#    newList[i].replace(newList[i][1], new0)
#newList.sort()
print(listt, alist, newList)
