ano = int(input("Informe seu ano de nascimento: "))

serv = 2020 - ano


if serv < 18:
    falta = 18 - serv
    alist = 2020 + falta
    print("Você nasceu em {}, tem {} anos em 2020. \nAinda faltam {} ano(s) para o seu alistamento.\nSeu alistamento será em {}.". format(ano, serv, falta, alist))
elif serv > 18:
    passou = serv - 18
    alist = 2020 - passou
    print("Você nasceu em {}, tem {} anos em 2020. \nJá deveria ter se alistado há {} ano(s). \nSeu alistamento foi em {}.".format(ano, serv, passou, alist ))
else:
    print("Você nasceu em {}, tem {} anos em 2020. Precisa se alistar IMEDIATAMENTE!".format(ano, serv))