from datetime import date
atual = date.today().year

nome = str(input('Informe seu nome: \n'))
nasc = int(input('Informe seu ano de nascimento: \n'))
idade = atual - nasc

print('Atleta {} tem {} anos.'.format(nome, idade))

if idade <= 9:
    print('Classificação: MIRIM')
elif idade <= 14:
    print('Classificação: INFANTIL')
elif idade <= 19:
    print('CLassificação: JUNIOR')
elif idade <= 25:
    print('Classificação: SÊNIOR')
else:
    print('Classificação: MASTER')