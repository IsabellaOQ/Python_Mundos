days = int(input("Informe a quantidade de dias: "))
km = float(input("Informe a quantidade de km's rodados: "))

preco = (days *60) + (km * 0.15)

print("Total: {:.2f}" .format(preco))