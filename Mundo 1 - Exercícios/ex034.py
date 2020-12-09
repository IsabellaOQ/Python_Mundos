sal = float(input("Infome seu salário, por favor: R$"))

if sal > 1250:
    cal = sal * 0.10
    aumento = sal + cal
    print("Com seu salário R${:.2f}, você obteve um aumento de R${:.2f}. \nSeu salário atual é: R${:.2f}.". format(sal, cal, aumento))
else:
    cal = sal * 0.15
    aumento = sal + cal
    print("Com seu salário R${:.2f}, você obteve um aumento de R${:.2f}. \nSeu salário atual é: R${:.2f}.".format(sal, cal, aumento))