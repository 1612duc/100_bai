a = int(input())
dem = 0
for i in range(1, a+1):
    if a % i == 0:
        dem += 1
print(dem)