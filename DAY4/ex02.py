a = input()
a.lower()
f = 0
for i in a:
    if i == "g" or i == "c":
        f += 1
d = f / len(a) * 100
print(d)
