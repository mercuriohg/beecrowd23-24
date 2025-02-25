hinicio, hfim = map(int,input().split())
maximo = 24
if hinicio < hfim:
    duracao = hfim - hinicio
else:
    duracao = maximo - hinicio + hfim

print("O JOGO DUROU {} HORA(S)".format(duracao))
