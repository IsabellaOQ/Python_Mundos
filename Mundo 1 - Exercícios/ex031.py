km = float(input("Informe a distância da viagem em Km, por favor: "))
if km <=200:
    valor = km * 0.50
    print("Sem desconto, o valor é de: {:.2f} reais.". format(valor))
else:
    valor = km * 0.45
    print("Com desconto, o valor é de: {:.2f} reais.". format(valor))