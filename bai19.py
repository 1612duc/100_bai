a = int(input())
b = int(input())
c = int(input())
if a != 0:
    delta = 2*b - 4*a*c
    if delta < 0:
        print("vô nghiệm")
    elif delta == 0:
        print(-b/a)
    else:
        print((-b+delta**0.5)/2)
        print((-b-delta**0.5)/2)
else:
    print("False")