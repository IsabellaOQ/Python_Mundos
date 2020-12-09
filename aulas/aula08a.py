import math
num = int(input('Digite um número: '))
raiz = math.sqrt(num)
print('A raiz de {} é igual a {}'.format(num, raiz))


print("\n OU: \n")


from math import sqrt, floor
num1 = int(input('Digite um número: '))
raiz1 = sqrt(num)
print('A raiz de {} é igual a {}'.format(num1, floor(raiz1)))


print("\n OUTRO EXEMPLO: \n")

import random
num = random.random()
num1 = random.randint(1, 10)
print(num, num1)

import emoji
print(emoji.emojize("Olá, Mundo :earth_americas:", use_aliases=True))

