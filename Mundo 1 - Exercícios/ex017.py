from math import hypot
cat1 = float(input("Informe o cateto oposto: "))
cat2 = float(input("Informe o cateto adjacente: "))
hip = hypot(cat1, cat2)

print("Cateto oposto {}, Cateto adjacente {}, Hipotenusa {:.2f}".format(cat1, cat2, hip))