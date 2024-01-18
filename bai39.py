n = int(input())
chan = le = 0
while  n > 0:
    if (n % 10) % 2 == 0:
        chan += 1
    else:
        le += 1
    n //= 10
print(chan, le)