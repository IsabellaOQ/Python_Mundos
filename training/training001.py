nome = str(input("Digite seu nome completo: ")).strip()
print(nome)
print("Analisando seu nome...")
print("Seu nome em maiúsculas é {}".format(nome.upper()))
print("Seu nome em minúsculas é {}".format(nome.lower()))
print("Seu nome tem ao todo {} letras".format(len(nome)))

nome1 = nome.split()

print("Seu primeiro nome é {} e ele tem {} letras".format(nome1[0].capitalize(),len(nome1[0])- nome1[0].count(' ')))