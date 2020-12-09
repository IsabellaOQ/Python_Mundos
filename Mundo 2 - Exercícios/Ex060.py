fatorial = 1
n = int(input('Digite um número para calcular seu fatorial: '))
menos = n

while menos > 0:
    fatorial = menos * fatorial
    menos = menos - 1
print('Seu fatorial é {}'. format(fatorial))