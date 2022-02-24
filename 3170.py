import math

B = int(input())
G = int(input())

divgalho = G / 2
divgalho = math.floor(divgalho)

if B == divgalho or B > divgalho:
    print("Amelia tem todas bolinhas!")

elif B < divgalho:
    rest = divgalho - B
    print("Faltam", rest, "bolinha(s)")
