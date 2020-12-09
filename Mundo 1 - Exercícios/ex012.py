n= float(input("Informe o seu salário atual: "))
n2= int(input("Informe a porcentagem de aumento: "))
p=(n*n2)/100
f=p+n
print("O valor de seu salário com os {}% de aumento vai ser igual à: {:.2f}. Parabéns!".format(n2, f))
