l = list(map(int, input().split()))
for i in range(1, len(l)):
    if l[i] < l[i-1]:
        print("False")
        break
else:
    print("True")