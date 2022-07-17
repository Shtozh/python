A = int(input())
Y = A % 4
if Y != 0:
    print('Обычный')
else:
   YY = A % 100
   if YY !=0:
       print('Високосный')
   else:
       YYY=A % 400
   if YYY==0:
       print('Високосный')
   else:
       print('Обычный')
