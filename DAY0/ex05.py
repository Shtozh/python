AA = input()
D = AA[AA.find("[") + 1:]
DD = D.partition(']')[0]
B = list(map(int, DD.split(",")))
BB = list(reversed(B))
print(BB)
#не знаю как обработать случай head = []