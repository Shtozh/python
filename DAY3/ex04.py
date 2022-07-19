nn = int(input())
if nn < 100:
    if nn % 10 == 0 or (5 <= nn % 10 <= 9) or (11 <= nn <= 14):
        print(int(nn), 'программистов')
    elif nn % 10 == 1 and nn != 11:
        print(int(nn), 'программист')
    elif 2 <= nn % 10 <= 4:
        print(int(nn), 'программиста')
else:
    if nn % 10 == 0 or (5 <= nn % 10 <= 9) or (11 <= nn % 100 <= 14):
        print(int(nn), 'программистов')
    elif nn % 10 == 1 and nn % 100 != 11:
        print(int(nn), 'программист')
    elif 2 <= nn % 10 <= 4:
        print(int(nn), 'программиста')

#ну тут да, один и тот же код получился для if и else
#если буду успевать, то надо переделать