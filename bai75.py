def ams(a):
    b = a
    tong = 0
    for i in range(len(str(a))):
        d = b % 10
        tong += d**len(str(a))
        b //= 10
    if tong == a:
        return True
    return False
a = int(input())
print(ams(a))