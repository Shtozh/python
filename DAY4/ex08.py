a = int(input())
k = 1
j = 0
if a > 0:
    while j < a:
        for i in range(k):
            print(k)
            j += 1
            if j >= a:
                break
        else:
            k += 1
