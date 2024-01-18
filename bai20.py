month = int(input())
year = int(input())
d31 = [1, 3, 5, 7, 8, 10, 12]
d30 = [4, 6, 9, 11]
if month in d31:
    print(31)
elif month in d30:
    print(30)
else:
    if year % 400 == 0 or (year % 4 == 0 and year % 100 != 0):
        print(29)
    else:
        print(28)