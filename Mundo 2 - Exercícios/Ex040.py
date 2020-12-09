n1 = float(input("Digite sua primeira nota: "))
n2 = float(input("Digite sua segunda nota: "))

media = (n1 + n2)/2

if media < 5.0:
    print("Com as notas {} e {}, você foi REPROVADO com a média {:.1f}!".format(n1, n2, media))
elif media <= 6.9:
    print("Com as notas {} e {}, você ficou de RECUPERAÇÃO com a média {:.1f}!".format(n1, n2, media))
else:
    print("Com notas tão boas você foi APROVADO com média {}". format(media))
