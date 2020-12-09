from random import randint
computador = randint(0, 10)
print('Computador : {}'.format(computador))
tent = 0

print('Sou seu computador...\nAcabei de pensar em um número entre 0 e 10.\nSerá que você consegue adivinhar qual foi?')
resp = int(input('Qual é o seu palpite?'))

while resp != computador:
    if(resp < computador ):
        resp = int(input('Mais...Tente mais uma vez: '))
        tent += 1
    else:
        resp = int(input('Menos...Tente mais uma vez: '))
        tent += 1

if(tent < 3):
    print('Acertou com {} tentativas. Parabéns!'.format(tent))
else:
    print('Acertou com {} tentativas. Parabéns, uma BOSTA!'.format(tent))