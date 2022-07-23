a = input()
for j in a:
    if j == " ":
        k = 1
        break
    else:
        k = 0
if k == 0:
    print(a)
else:
    B = list(map(int, a.split(" ")))
    D = list(map(int, a.split(" ")))
    k = len(B)
    D[0] = B[1]+B[k-1]
    D[k - 1] = B[k - 2] + B[0]
    for i in range(k-1):
        if i != 0:
            D[i] = B[i-1] + B[i+1]
    else:
        for ii in range(len(D)):
            print(D[ii],end=" ")


