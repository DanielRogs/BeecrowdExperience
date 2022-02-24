X = int(input())

Z = 0
while Z <= X:
    Z = int(input())

contador = 0
while X < Z:

    X = X + (X + 1)
    contador += 1
    

print(int(contador + 2))
