a = input()
so = "0123456789"
tong = 0
for i in a:
    if i in so:
        tong += int(i)
print(tong)