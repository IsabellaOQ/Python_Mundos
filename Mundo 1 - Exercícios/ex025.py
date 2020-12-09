#nome = str(input("Qual é o seu nome completo? ")).strip().upper().split()
#print("Seu nome tem Silva? {}".format(nome.__contains__('SILVA')))

# OU

nome = str(input("Qual é o seu nome completo? ")).strip().lower()
print("Seu nome tem Silva? {}".format('silva' in nome))
