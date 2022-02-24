#Entrada da quantidade de números
quant = int(input())
quant -= 1

num = input().split()


Qmult2 = 0
Qmult3 = 0
Qmult4 = 0
Qmult5 = 0

while quant >= 0:

  
    if int(num[quant]) % 2 == 0: 
        Qmult2 += 1 
    
    
    if int(num[quant]) % 3 == 0:
        Qmult3 += 1


    if int(num[quant]) % 4 == 0:
        Qmult4 += 1

   
    if int(num[quant]) % 5 == 0:
        Qmult5 += 1

   
    
    quant -= 1

print('{} Multiplo(s) de 2'.format(Qmult2))
print('{} Multiplo(s) de 3'.format(Qmult3))
print('{} Multiplo(s) de 4'.format(Qmult4))
print('{} Multiplo(s) de 5'.format(Qmult5))
