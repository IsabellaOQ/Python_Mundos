from random import randint

print("Vou pensar em um núemro e quero ver você adivinhar qual foi...")
comp = randint(0 , 5)

numero = int(input('Digita aí: '))
print("Analisando os dados...")

print('-=-' *20) #coloquei isso só pra fazer graça :)
if numero == comp:
    print("Parabéns!! Você chutou certinho :)")
else:
    print("Putss, errou, que pena!")
print('-=-' *20)