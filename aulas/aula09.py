frase = 'Curso em Vídeo Python'

''' aqui os espaços da frase também contam!

 o 1° número = onde começa; 
 o 2° número = onde vai terminar;
 o 3° número = a quantidade que ele vai ter que ir pulando'''

print(frase + "\n")
print(frase[3] + "\n")
print(frase [3:13] + "\n")
print(frase [:13] + "\n")
print(frase[1:15:2] + "\n")
print(frase [1::2] + "\n")
print(frase [::2] + "\n")

print(""" \nWelcome! Are you completely new to programming? 
about why and how to get started with Python. Fortunately 
an experienced programmer in any programming language 
whatever it may be) can pick up Python very quickly. 
It's also easy for beginners to use and learn, so jump in! \n """)

print(frase.count('o'))
print(frase.count('O'))
print(frase.upper().count('O'))
print(len(frase))

print("\n")

#lstrip = corta os espaços da esquerda; rstrip = corta os da direita; strip = corta dos dois
frase1 = '   Curso em Vídeo   '
print(len(frase1))
print(len(frase1.strip()))
print(len(frase.lstrip()))
print(len(frase.rstrip()))
print(frase1.replace('Vídeo', 'Android'))

print("\n")

frase2 = 'Curso em Vídeo Python'
print(frase2)
print(frase2.replace('Python', 'Android'))
print(frase2) #perceba que ela não permaneceu alterado, portanto:
print("\n")

frase2 = frase2.replace('Python', 'Android')
print(frase2)

print("\n")

print('Curso' in frase2)
print(frase2.find('Curso'))
print(frase2.find('Android'))
print(frase2.find('Bella')) # -1 representa que não foi encontrado

print("\n")

dividido = frase2.split()
print(dividido)
print(dividido[0])
print(dividido[2])
print(dividido[2][3])
