n = int(input("Digite um número: "))

c = 0

for i in range (1, n + 1):
    if n % i == 0 and n % 1 == 0 and n % n == 0:
        c = c +1

if c > 2:
    print("O número NÃO É PRIMO!")
else:
    print("O número é PRIMO!")

