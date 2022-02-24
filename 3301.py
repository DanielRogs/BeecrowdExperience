HZL = input().split()

H = int(HZL[0])
Z = int(HZL[1])
L = int(HZL[2])

if (H > Z and H < L) or (H < Z and H > L):
    print("huguinho")

if (Z > H and Z < L) or (Z < H and Z > L):
    print("zezinho")

if (L > H and L < Z) or (L < H and L > Z):
    print("luisinho")
