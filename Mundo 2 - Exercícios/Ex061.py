print('Gerador de PA \n*------*------*------*------*')

n = int(input('Primeiro termo da PA: '))
r = int(input('Razão da PA: '))
print(n, end='  ')

termo = 0
soma = r


while termo < 9:
    n = soma + n
    termo += 1

    print(n, end='  ')

