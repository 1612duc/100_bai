def snt(n):
    if n < 2:
        return False
    if n == 2:
        return True
    for i in range(2, int(n**0.5)):
        if n % i == 0:
            return False
    return True
a = int(input())
print(snt(a))