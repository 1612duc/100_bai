a = input()
so = "0123456789"
tong = 0
tmp = ""
for i in a:
    if i in so:
        tmp += i
    elif tmp != "":
        tong += int(tmp)
        tmp = ""
print(tong)