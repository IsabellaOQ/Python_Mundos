nome = str(input("Digite seu nome completo: ")).strip().split()
print("Muito prazer em te conhecer, {}!".format(nome[0].capitalize()))
print("Seu primeiro nome é {}".format(nome[0].capitalize()))
print("Seu último nome é {}".format(nome[len(nome)-1].capitalize()))

#print(nome)


# Usei esse capitalize() para deixar a primeira letra em maiúsculo.