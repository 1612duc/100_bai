n = int(input())
d = 0
kq = []
for i in range(1, n):
    s = 0
    a = []
    while s < n:
        s += i
        i += 1
        a.append(str(i))
    if s == n:
        d += 1
        kq. append(a)
print(d)
for i in kq:
    print("+".join(i))