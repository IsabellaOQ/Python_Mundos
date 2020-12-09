from math import sin, cos, tan, radians
num = float(input('Informe o valor do ângulo: '))
sen = sin(radians(num))
cos = cos(radians(num))
tan = tan(radians(num))

'''Coloquei esse math.radians dentro da função porque de acordo com o documento do python,
 o seno, cosseno e tangente vêm em radianos, por isso tive que converter :) ♥'''


print('O valor do SENO é {:.2f} \n O valor do COSSENO é {:.2f} \n O valor da TANGENTE é {:.2f}'. format(sen, cos, tan))