X = int(input())
H = int(input())
M = int(input())
Y = X//60
YY = X % 60
HH = H+Y
MM = M+YY
HHH = HH + MM//60
MMM = MM % 60
print(HHH)
print(MMM)