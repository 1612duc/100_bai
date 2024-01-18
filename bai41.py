n = int(input())
while n > 1:
    if n % 2 != 0:
        print("False")
        break
    n //= 2
else:
    print("True")