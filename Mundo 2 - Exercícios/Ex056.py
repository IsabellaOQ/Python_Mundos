maior = 0
menor = 0
menosVinte = 0
somaidade = 0
p = ''


for pessoas in range(1, 5):
    nome = str(input('Nome: ')).capitalize()
    idade = int(input('Idade: '))
    sexo = str(input('Sexo [F/M]: ')).lower()
    print('\n')

    somaidade += idade


    if pessoas == 1 and sexo == 'm':
         maior = idade
         menor = idade
         p = nome

    elif sexo == 'm':
        if idade > maior:
            maior = idade
            p = nome
        if idade < menor:
            menor = idade
            p = nome


    if sexo == 'f':
        if idade < 20:
             menosVinte = menosVinte +1

mediaidade = somaidade/4


print('A média das idades é: {} anos'.format(mediaidade))
print('O nome do homem mais velho é: {} e tem {} anos'.format(p, maior))
print('Mulheres abaixo de 20 anos: {}'.format(menosVinte))