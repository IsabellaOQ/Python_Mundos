ano = int(input("Ano de nascimento: "))

ano1 = 2020 - ano

if ano1 <= 9:
    print("Classificação: MIRIM")
elif ano1 <= 14:
    print("Classificação: INFANTIL")
elif ano1 <= 19:
    print("Classificação: JUNIOR")
elif ano1 <= 25:
    print("Classificação: SÊNIOR")
else:
    print("Classificação: MASTER")