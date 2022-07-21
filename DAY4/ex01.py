a = int(input())
b = int(input())
c = int(input())
d = int(input())
print('\t', end = "")
for number in range(c,d+1):
        print(number, end = "\t")

print('\n')
for i in range(a,b+1):
    print(i, end="\t")
    for j in range(c,d+1):
        print(i*j,end="\t")
        if j == d:
            print('\n')