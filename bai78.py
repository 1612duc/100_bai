def mi(a):
    d = a[0]
    for i in a:
        if len(i) < len(d):
            d = i
    return d
a = input().split()
print(mi(a))