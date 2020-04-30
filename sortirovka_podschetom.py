def CountSort(a):
    alist = [0] * (max(a) + 1)
    for i in a:
        alist[i] += 1
    for n in range(len(alist)):
        for i in range(alist[n]):
            print(n, end=' ')
    return ' '
nums = list(map(int, input().split()))
print(CountSort(nums))
