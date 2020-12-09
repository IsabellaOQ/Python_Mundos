cont= n = media = soma = maior = menor= 0
opcao = "S"

while opcao in 'S':
    n = int(input('Digite um número: '))
    opcao = str(input('Quer continuar? [S/N] ')).upper()
    cont += 1
    soma = soma + n

    if cont == 1:
        maior = n
        menor = n
    elif n > maior:
        maior = n
    elif n < menor:
        menor = n

    while opcao not in 'SN':
        opcao = str(input('Opção inválida. Tente novamente! ')).upper()

media= soma/cont
print('Você digitou {} valores e a média foi {}.'.format(cont, media))
print('O maior valor foi {} e o menor foi {}'.format(maior, menor))
