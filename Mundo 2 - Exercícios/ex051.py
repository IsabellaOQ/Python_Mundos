print("=" * 40)
print("          10 TERMOS DE UMA PA")
print("=" * 40)

n = int(input("Primeiro termo: "))
r = int(input("Razão: "))

decimo = n + (10 - 1) * r #FÓRMULA PRA CALCULAR O DÉCIMO N°

for i in range (n, decimo, r):
    print(i,"-> ", end=" ")
print("ACABOU! :)")

