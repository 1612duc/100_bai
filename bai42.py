n = int(input())
a = b = 1
c = 2
while b <= n:
    a = b
    b = c
    c += a
print(a)