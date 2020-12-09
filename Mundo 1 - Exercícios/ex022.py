nome = str(input('Digite seu nome completo: ')).strip()
print("Analisando seu nome...")
print("Seu nome em maiúsculas " + nome.upper())
print("Seu nome em minúsculas " + nome.lower())
print("Seu nome tem {} letras.".format(len(nome.replace(' ', ''))))
#print("Seu primeiro tem {} letras.".format(nome.find(' ')))


dividido = nome.split()
print("Seu primeiro nome é {} e ele tem {} letras".format(dividido[0], len(dividido[0])))
