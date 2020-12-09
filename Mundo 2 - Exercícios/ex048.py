s =0
c =0
for i in range (1, 501, 2):
   # print(i, end = " ")

    if i % 3 == 0:
        c = c + 1
        s = s +i
print("O valor total dos {} valores é: {}".format(c,s))
