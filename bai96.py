def uoc(x):
    tong = 1
    for i in range(2, int(x/2) + 1):
        if x % i == 0:
            tong += i
    return tong

k = int(input())
for m in range(1, k):
    n = uoc(m)
    if m > n and uoc(m) == n and uoc(n) == m:
        print(m, n)