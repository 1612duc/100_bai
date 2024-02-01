def kc(ax, ay, bx, by):
    d = ((bx-ax)**2 + (by-ay)**2)**0.5
    return d

n = int(input())
dem = 0
x = []
y = []
for i in range(n):
    a, b = map(int, input().split())
    x.append(a)
    y.append(b)

for i in range(n-2):
    for j in range(i+1, n-1):
        for k in range(j+1, n):
            a = kc(x[i], y[i], x[j], y[j])
            b = kc(x[i], y[i], x[k], y[k])
            c = kc(x[j], y[j], x[k], y[k])
            if (a == b or b == c or c == a) and a+b>c and b+c>a and c+a>b:
                dem += 1
print(dem)