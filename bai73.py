def bcc(a, b):
    a = max(a, b)
    for i in range(1, 11):
        print(a, "*", i, "=", a*i)
    return ""
a = int(input())
b = int(input())
print(bcc(a, b))