import string

alfabeto = list(string.ascii_uppercase)

alfabeto.insert(0, None)

letra = input()

print(alfabeto.index(letra))
