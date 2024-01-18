t = float(input())
v = float(input())
a = float(input())
tb = (t + v + a) / 3
if tb >= 8 and (t >= 8 or v >= 8) and t >= 6.5 and v >= 6.5 and a >= 6.5:
    print("giỏi")
elif tb >= 6.5 and (t >= 6.5 or v >= 6.5) and t >= 5 and v >= 5 and a >= 5:
    print("khá")
elif tb >= 5 and (t >= 5 or v >= 5) and t >= 3.5 and v >= 3.5 and a >= 3.5:
    print("trung bình")
elif tb >= 3.5 and (t >= 3.5 or v >= 3.5) and t >= 2 and v >= 2 and a >= 2:
    print("yếu")
else:
    print("kém")