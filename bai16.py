a = int(input())
b = int(input())
c = int(input())
a = max(a,b,c)
b = a+b+c-max(a,b,c)-min(a,b,c)
c = min(a,b,c)
if a + b > c and b + c > a and c + a > b:
    if a == b == c:
        print("đều")
    elif b**2 + c**2 == a**2 and b == c:
        print("vuông cân")
    elif b**2 + c**2 == a**2:
        print("vuông")
    elif b == c:
        print("cân")
    else:
        print("thường")
else:
    print("False")