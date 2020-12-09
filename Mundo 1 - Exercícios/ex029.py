velo = float(input("Por favor, informe a velocidade do carro: "))
multa = (velo-80 )*7
if velo > 80:
    print('VOCÊ FOI MULTADO! A multa que deverá pagar é de {:.2f} reais.'.format(multa))
else:
    print('Você está dentro do limite de velocidade!')
print('Dirija com cuidado :)')