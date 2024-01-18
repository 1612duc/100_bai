a = input()
s = "0123456789"
b = a.upper()
hoa = thuong = so = 0
for i in range(len(a)):
    if a[i] == b[i]:
        hoa += 1
    elif a[i] in s:
        so += 1
    else:
        thuong += 1
print(hoa, thuong, so)