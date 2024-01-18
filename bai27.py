h = int(input())
for i in range(1, h+1):
    print("* " * i)
for i in range(1, h+1):
    for j in range(1, h-i+1):
        print(" ", end = "")
    print("* " * i)