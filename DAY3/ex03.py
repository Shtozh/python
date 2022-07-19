a = int(input())
b = int(input())
c = int(input())
Max = max([a, b, c])
Min = min([a, b, c])
print(Max)
print(Min)
if a != Max and a != Min:
    print(a)
elif b != Max and b != Min:
    print(b)
else:
    print(c)