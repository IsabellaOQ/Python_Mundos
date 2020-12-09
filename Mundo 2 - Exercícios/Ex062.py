print('Gerador de PA \n*------*------*------*------*')

n = int(input('Primeiro termo da PA: '))
r = int(input('Razão da PA: '))
print(n, end="  ")
termo = n
cont = 1
total = 0
mais = 10

while mais > 0:
    total = total + mais
    while cont < total:
        termo += r
        cont += 1
        print(termo, end="  ")
    print('--> PAUSA')
    mais = int(input('Quantos termos você quer mostrar a mais?'))
print('Progressão finalizada com {} termos mostrados.'.format(total))
