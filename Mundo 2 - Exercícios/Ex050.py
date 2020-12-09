s=0
c=0
for i in range (0, 6):
    n = int(input("Informe o n°: "))

    if n % 2 == 0:
        c = c +1
        s = s + n

if s > 0:
    print("A soma dos {} números pares foi {}.".format(c, s))
else:
    print("Não houveram números pares!")
