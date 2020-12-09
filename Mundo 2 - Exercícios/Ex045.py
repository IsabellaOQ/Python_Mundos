from random import randint

jog = int(input("Suas opções: \n[ 0 ] PEDRA \n[ 1 ] PAPEL \n[ 2 ] TESOURA \nQual a sua jogada?"))

if jog == 0:
    escolha = 'PEDRA'
elif jog == 1:
    escolha = 'PAPEL'
elif jog == 2:
    escolha = 'TESOURA'
else:
    print("Número inválido, tente de novo!")
    breakpoint()


comp = randint(0,2)

if comp == 0:
    escolha1 = 'PEDRA'
elif comp == 1:
    escolha1 = 'PAPEL'
else:
    escolha1 = 'TESOURA'



print("JÔ")
print("KEN")
print("PÔ!!!")


print("-=-" * 10)
print("Computador jogou {}.". format(escolha1))
print("Jogador jogou {}.".format(escolha))
print("-=-" * 10)

if jog != comp:
    if jog == 0 and comp == 1 or jog == 1 and comp == 2:
        print("COMPUTADOR VENCEU!")
    else:
        print("JOGADOR VENCEU!!")
else:
    print('EMPATE!!!')


