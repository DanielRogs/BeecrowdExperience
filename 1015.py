linha1 = input().split()
x1 = float(linha1[0])
y1 = float(linha1[1])

linha2 = input().split()
x2 = float(linha2[0])
y2 = float(linha2[1])

math1 = (x2 - x1)**2
math2 = (y2 - y1)**2

math1 = math1 + math2

math1 = math1**0.5

print(round(math1, 4))
