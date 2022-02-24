M = 0
A = 0
B = 0

while M < 40 or M > 110 or A == B or A < 1 or B < 1 or  A > M or B > M:
    M = int(input())
    A = int(input())
    B = int(input())

math1 = A + B
C = M - math1

if A > B and A > C:
    print(A)

if B > A and B > C:
    print(B)

if C > B and C > A:
    print(C)
