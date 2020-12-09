l1 = float(input("Digite o primeiro lado: "))
l2 = float(input("Digite o segundo lado: "))
l3 = float(input("Digite o terceiro lado: "))

if l1 + l2 > l3 and l2 + l3 > l1 and l3 + l1 > l2:
    print("\033[4;30;45mAs retas PODEM formar um triângulo!\033[m")
else:
    print("\033[1;31;40mAs retas NÃO FORMAM um triângulo!\033[m")

#Usei esse \033 só para formatar as cores que queria, aula 11 do Curso em Vídeo