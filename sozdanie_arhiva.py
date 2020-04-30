s = list(map(int, input().split()))
alist = []
for i in range(0, s[1]):
    n = int(input())
    alist.append(n)
summa = 0
count = 0
alist.sort()
if s[0] >= alist[0]:
    for i in range(0, s[1]):
        summa += alist[i]
        if summa >= s[0]:
            break
        count += 1
    if count == 0:
        count += 1
    if s[0] == 0:
        print('0')
    else:
        print(count)
else:
    print('0')
