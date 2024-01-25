def abc(a, k):
    for i in a:
        if i == k:
            return a.index(i)
    return -1
a = list(map(int, input().split()))
k = int(input())
print(abc(a, k))