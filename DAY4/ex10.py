def modify_list(l):
     a = l
     j = 0
     #ll=len(l)-2
     ll=len(l)
     for i in range(ll):
       #  print(l[i])
         if (int(l[i-j]) % 2) != 0:
             l.pop(i-j)
             ll=len(l)
             j+=1
         else:
             l[i-j] = int(int(l[i-j])/ 2)
             ll = len(l)
'''             
lst = [1, 2, 3, 4, 5, 6]
print(modify_list(lst))
print(lst)
modify_list(lst)
print(lst)

lst = [10, 5, 8, 3]
modify_list(lst)
print(lst)
'''