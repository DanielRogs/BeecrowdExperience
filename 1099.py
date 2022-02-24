N = int(input())

for i in range(N):
    XY = input().split()

    X = int(XY[0])
    Y = int(XY[1])

    som = 0
    if X < Y:
        while not X == (Y-1):
            X += 1
            if X % 2 != 0:
                som += X

    if Y < X:
        while not Y == (X-1):
            Y += 1
            if (Y % 2) != 0:
                som += Y
    print(som)
