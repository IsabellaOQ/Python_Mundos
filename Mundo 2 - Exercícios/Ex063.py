print('*-----*' *4)
print('SEQUÊNCIA DE FIBONACCI')
print('*-----*' *4)

n = int(input('\nQuantos termos você quer mostrar? '))

primeiro = 0
segundo = 1
cont = 0
atual = 0
sequencia = 0
print('{}  {}'.format(primeiro, segundo), end="  ")


while cont < n-2:

    if cont==0:
        atual = segundo
        cont += 1

    else:
        primeiro = segundo
        segundo = atual
        cont += 1
    sequencia = atual + primeiro
    atual = sequencia


    print(sequencia, end= "  ")
print('\n')

""" -----COMENTÁRIO-----

-------- OUTRA FORMA DE CÓDIGO: SIMPLIFICADO :) --------


print('*-----*' *4)
print('SEQUÊNCIA DE FIBONACCI')
print('*-----*' *4)

n = int(input('\nQuantos termos você quer mostrar? '))

primeiro = 0
segundo = 1
cont = 2
atual = 0
sequencia = 0
print('{} '.format(primeiro), end=' ')


while cont < n:
    primeiro = segundo
    segundo = atual
    sequencia = atual + primeiro
    atual = sequencia
    cont += 1

    print(sequencia, end= "  ")
print('\n')


"""




