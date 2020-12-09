soma =0
mult = 0


n1 = int(input('Primeiro valor: '))
n2 = int(input('Segundo valor: '))

opcao = int(input('[ 1 ] Somar \n[ 2 ] Multiplicar \n[ 3 ] Maior \n[ 4 ] Novos números \n[ 5 ] Sair do programa \n>>>>> Qual a sua opção:  '))

while opcao != 5:
    if (opcao == 1):
        soma = n1 + n2
        print('A soma entre {} e {} é {}'.format(n1, n2, soma))

    elif (opcao == 2):
        mult = n1 * n2
        print('A multiplicação entre {} e {} é {}'.format(n1, n2, mult))

    elif (opcao == 3):
        if (n1 > n2):
            print('O maior é {}'.format(n1))
        else:
            print('O maior é {}'.format(n2))

    elif (opcao == 4):
        n1 = int(input('Primeiro valor (2ª vez):'))
        n2 = int(input('Segundo valor (2ª vez): '))

    elif (opcao not in range(1, 4)):
        print('Opção inválida, tente novamente: ')

    opcao = int(input('[ 1 ] Somar \n[ 2 ] Multiplicar \n[ 3 ] Maior \n[ 4 ] Novos números \n[ 5 ] Sair do programa \n>>>>> Qual a sua opção:  '))





print('Finalizando...')