N = int(input())

AB = input().split()

A = int(AB[0])
B = int(AB[1])

hour = A + B

if hour <= N:
    print ("Farei hoje!")

else:
    print ("Deixa para amanha!")
