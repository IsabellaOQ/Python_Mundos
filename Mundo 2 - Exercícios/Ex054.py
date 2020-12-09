from datetime import date

dataAtual = date.today().year
maioridade = 0
menoridade = 0

for pessoas in range(1, 8):
    nasc = int(input('Em que ano nasceu a {}ª pessoa: '.format(pessoas)))
    idade = dataAtual - nasc

    if idade >= 18:
        maioridade = maioridade + 1
    else:
        menoridade = menoridade + 1

print('Ao todo tivemos {} pessoas maiores de idade.'.format(maioridade))
print('E também tivemos {} pessoas menores de idade.'.format(menoridade))


