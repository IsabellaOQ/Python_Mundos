valor = float(input("Informe o valor da casa: R$"))
sal = float(input("Informe seu salário: R$"))
anos = int(input("Informe em quantos anos vai querer pagar: "))

prestacao = valor/(anos*12)

excede = sal * 0.30

if prestacao > excede:
    print("\nEmpréstimo negado, salário muito baixo para prestação do imóvel. \nSalário: R${:.2f} \nPrestação: R${:.2f}".format(sal, prestacao))
else:
    print("\nEmpréstimo concedido! \nPrestação de R${:.2f} por mês, durante {} anos.".format(prestacao, anos))
