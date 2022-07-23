print("Напишите целые числа через пробел. Например:5 10 1")
a = input()
B = list(map(int, a.split(" ")))
d = 0
for i in range(len(B)):
    d += int(B[i])
else:
    print(d)