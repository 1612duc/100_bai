def snt(n):
    if n < 2:
        return False
    if n == 2:
        return True
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True
def abc(a, n):
    b = []
    for i in a:
        if snt(i) == True and len(b) < n:
            b.append(i)
    return b
a = list(map(int, input().split()))
n = int(input())
print(abc(a, n))