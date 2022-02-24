l1 = input().split()

A = int(l1[0])
B = int(l1[1])
C = int(l1[2])

math1 = A + B - C
math2 = A + C - B
math3 = B + C - A

if math1 == 0 or math2 == 0 or math3 == 0:
    print("S")

else:
    math1 = A - B
    math2 = A - C
    math3 = B - C

    if math1 == 0 or math2 == 0 or math3 == 0:
        print("S")
    
    else:
        print("N")
