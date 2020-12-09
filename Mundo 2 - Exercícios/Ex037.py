import math

n = int(input("Informe o número que deseja converter: "))
base = int(input("Informe a base de conversão que deseja: \n[1] Binário \n[2] Octal \n[3] Hexadecimal\n"))

if base == 1:
    print("{} convertido para binário é {}.".format(n, bin(n) [2:]))
elif base == 2:
    print("{} convertido para octal é {}.".format(n, oct(n)[2:]))
else:
    print("{} convertido para hexadecimal é {}.".format(n, hex(n)[2:]))

#usei esse [2:] para cortar os dois primeiros "números" que aparecem (pq são de máquina),
# aprendi isso na aula de fatiamento.
