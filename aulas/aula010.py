nome = str(input("Digite seu nome, por favor: ")).capitalize()
if nome == 'Isabella':
    print("Que nome lindo você tem!")
else:
    print("Seu nome é tão normal!")

print('Bom dia, {}!'.format(nome))

#Só usei o capitalze() pra deixar a primeira letra em maiúscula, por estética mesmo! :)

#OUTRO EXEMPLO

n1 = float(input("Digite a primeira nota: "))
n2 = float(input('Digite a segunda nota: '))
media = (n1+ n2)/2

print("A sua média foi {:.1f}".format(media))
if media >= 6.0:
    print("Sua média foi boa! PARABÉNS")
else:
    print("Sua média foi ruim! ESTUDE MAIS")

#posso substituir esse if e else por um simplificado:
#print('PARABÉNS' if media>=6 else 'ESTUDE MAIS!')