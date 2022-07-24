a = input()
k = 0
for i in a:
    for j in a:
        if j == i:
            k += 1
    else:
        if k <= 1:
            print(i,end=" ")
            k = 0
        else:
            k = 0





















