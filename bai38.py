n = int(input())
dem = 0
while  n > 0:
    n //= 10
    dem += 1
print(dem)