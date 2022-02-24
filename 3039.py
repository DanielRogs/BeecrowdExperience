N = int(input())


car = 0
bon = 0


while N != 0:
    
    NS = input().split()
    No = NS[0]
    S = NS[1].upper()


    if S == 'M':
        car += 1 
    else:
        bon += 1
    
    N -= 1

print('{} carrinhos'.format(car))
print('{} bonecas'.format(bon))
