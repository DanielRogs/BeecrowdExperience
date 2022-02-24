N = int(input())



while N != 0: 
   
    MPontuacao = 0
    JPontuacao = 0
 
    V = 0


    while V < 3: 
        JXD = input().split()
        JX = int(JXD[0])
        JD = int(JXD[1])

        JPontuacao = JPontuacao + (JX * JD)
        V += 1

  
    V = 0

    while V < 3: 
        MXD = input().split() 
        MX = int(MXD[0])
        MD = int(MXD[1]) 

        MPontuacao = MPontuacao + (MX * MD) 
        V += 1
    
   
    if JPontuacao > MPontuacao: 
        print('JOAO') 

   
    else:
        print('MARIA') 


    N -= 1
