def ma(a):
    d = 0
    for i in a:
        if i > d:
            d = i
    return d
a = list(map(int, input().split()))
print(ma(a))