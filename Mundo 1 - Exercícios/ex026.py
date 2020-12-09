frase = str(input("Digite uma frase: ")).strip().upper()
#print(frase)
print("A letra A aparece {} vezes na frase".format(frase.count('A')))
print("A letra A aparece pela primeira vez na posição {}".format(frase.find('A') +1))
print("A letra A aparece pela última vez na posição {}".format(frase.rfind('A') +1))

#começa do zero, coloquei esses +1 por causa do usuário, pq ele vai contar a partir do 1, né... :)