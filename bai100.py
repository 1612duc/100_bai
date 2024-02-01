n = int(input())
d = 0
kq = []
for i in range(1, n):
    s = 0
    a = []
    while s < n:
        s += i
        a.append(str(i))
        i += 1
    if s == n:
        d += 1
        kq. append(a)
print(d)
for i in kq:
    print("+".join(i))