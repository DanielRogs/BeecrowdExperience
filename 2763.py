cpf = input()

cpf = cpf.split(".")
fn = cpf[2].split("-")
cpf.append(0)

cpf[2] = fn[0]
cpf[3] = fn[1]

print(cpf[0])
print(cpf[1])
print(cpf[2])
print(cpf[3])
