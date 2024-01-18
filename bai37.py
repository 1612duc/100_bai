a = 0
b = 10**9
while True:
    n = int(input())
    if n == -1:
        break
    if n > a:
        a = n
    if n < b:
        b = n
print(a, b)