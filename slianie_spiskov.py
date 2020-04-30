def merge(a, b):
    k = 0
    l = 0
    alist = []
    while k < len(a) and l < len(b):
        if a[k] < b[l]:
            alist.append(a[k])
            k += 1
        else:
            alist.append(b[l])
            l += 1
    alist += a[k:] + b[l:]
    return alist
a = list(map(int, input().split()))
b = list(map(int, input().split()))
print(*merge(a, b))
