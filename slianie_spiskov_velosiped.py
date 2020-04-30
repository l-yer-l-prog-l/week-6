def merge(a, b):
    alist = []
    count = 1
    len1 = len(a)
    len2 = len(b)
    if min(a) <= min(b):
        alist.append(min(a))
        alist.append(min(b))
    else:
        alist.append(min(b))
        alist.append(min(a))
    if len1 > len2:
        for i in range(1, len2):
            if alist[0] <= b[i] <= alist[1]:
                alist.insert(1, b[i])
                count += 1
            elif alist[count] < b[i]:
                alist.append(b[i])
            elif alist[count - 1] <= b[i] <= alist[count]:
                alist.insert(count, b[i])
            if alist[0] <= a[i] <= alist[1]:
                alist.insert(1, a[i])
                count += 1
            elif alist[count] < a[i]:
                alist.append(a[i])
            elif alist[count - 1] <= a[i] <= alist[count]:
                alist.insert(count, a[i])
            if i == 1:
                count = 1
            elif count >= len2 - 1:
                count += 0
            else:
                count += 1
        for i in range(len2, len1):
            if alist[0] <= a[i] <= alist[1]:
                alist.insert(1, a[i])
                count += 1
            elif alist[count] < a[i]:
                alist.append(a[i])
            elif alist[count - 1] <= a[i] <= alist[count]:
                alist.insert(count, a[i])
            if i == 1:
                count = 1
            elif count >= len1 - len2:
                count += 0
            else:
                count += 1
        return alist
    else:
        for i in range(1, len1):
            if alist[0] <= b[i] <= alist[1]:
                alist.insert(1, b[i])
                count += 1
            elif alist[count] < b[i]:
                alist.append(b[i])
            elif alist[count - 1] <= b[i] <= alist[count]:
                alist.insert(count, b[i])
            if alist[0] <= a[i] <= alist[1]:
                alist.insert(1, a[i])
                count += 1
            elif alist[count] < a[i]:
                alist.append(a[i])
            elif alist[count - 1] <= a[i] <= alist[count]:
                alist.insert(count, a[i])
            if i == 1:
                count = 1
            elif count >= len1 - 1:
                count += 0
            else:
                count += 1
        for i in range(len1, len2):
             if alist[0] <= b[i] <= alist[1]:
                alist.insert(1, b[i])
                count += 1
            elif alist[count] < b[i]:
                alist.append(b[i])
            elif alist[count - 1] <= b[i] <= alist[count]:
                alist.insert(count, b[i])
            if i == 1:
                count = 1
            elif count >= len2 - len1:
                count += 0
            else:
                count += 1
        return alist
nums1 = list(map(int, input().split()))
nums2 = list(map(int, input().split()))
print(*merge(nums1, nums2))
