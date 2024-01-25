def tb(a, n):
    return (n + a[0]) / 2
a = list(map(int, input().split()))
n = int(input())
print(tb(a, n))