n = int(input())
tong = 0
for i in range(n):
    a, b = map(int, input().split())
    tong += -a + b
print(tong)