a = int(input())
b = int(input())
c = int(input())
a = max(a,b,c)
b = a+b+c-max(a,b,c)-min(a,b,c)
c = min(a,b,c)
print(c, b, a)