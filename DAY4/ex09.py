def func1(x):
    if x <= -2:
        y = 1 - (x+2)*(x+2)
        print(y)
    elif -2 < x <= 2:
        y = -x/2
        print(y)
    elif 2 < x:
        y = (x-2)*(x-2) + 1
        print(y)
x = 1
func1(x)
