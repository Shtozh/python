a = input()
b = 1
k = len(a)-1
if k == 0:
    print(a[0]+str(b),end="")
for i in range(k):
    if i == (k - 1):
        if a[i] == a[i+1]:
            b += 1
            print(a[i]+str(b), end="")
        else:
            print(a[i]+str(b)+a[i+1]+str(1),end="")
    elif a[i] == a[i+1]:
        b += 1
    else:
        print(a[i]+str(b),end="")
        b=1



#for i in range(k): # i=0,1; len(a)=2 a[0],a[1], for i = 0, a-1, i = 0
  #  if a[i] == a[i+1]:
  #     b += 1
 #   elif i == k-1:
  #      print(22)
  #  elif i == range(k) and a[i] != a[i+1]:
   #        print(a[i + 1]+str(1), end="")
   # else:
    #    print(a[i]+str(b),end='')
     #   b = 1
