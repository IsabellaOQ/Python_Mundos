p1= float(input("Qual o preço do produto fora da liquidação? "))
l= int(input("Qual a porcentagem da liquidação? "))
n= (p1*l)/100
n1= p1-n
print("O valor do produto dentro da liquidação é igual à: R${:.2f}".format(n1))