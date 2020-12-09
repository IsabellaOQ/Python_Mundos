for i in range (0, 6):
    print(i)
print("FIM! \n") #vai contar do zero até o 5, pq ignora o último número

for i in range(6, 0, -1):
    print(i)
print("FIM! \n")  #vai contar do 6 até o 1, tirando de 1 em 1

for i in range(0, 7, 2):
    print(i)
print("FIM! \n")  #vai contar do zero ate o 7, pulando de 2 em 2


#EXEMPLOS:



n = int(input("Digite um número: "))
for i in range (0, n+1):  #coloquei o n+1 pra na contagem ele não descartar o n° que a pessoa escreveu
    print(i)
print("FIM! \n")

i = int(input("Início: "))
f= int(input("Fim: "))
p = int(input("Passo: "))
for c in range (i, f+1, p):
    print(c)
print("FIM! \n")