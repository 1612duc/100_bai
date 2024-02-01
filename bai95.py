n = int(input())
a = [0, 1, 1, 1]
if n <= 3:
    print(1)
else:
    for i in range(4, n+1):
        x = a[i-1] + a[i-3]
        a.append(x)
    print(a[n])