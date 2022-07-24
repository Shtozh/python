k = 0
d = 0
f = 0
while k == 0:
    a = int(input())
    d += a
    f += a*a
    if d == 0:
        k = 1
else:
    print(f)
