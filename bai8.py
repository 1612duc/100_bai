a = int(input())
if a < 2:
    print("False")
elif a == 2:
    print("True")
else:
    for i in range(2, int(a**0.5)+1):
        if a % i == 0:
            print("False")
            break
    else:
        print("True")