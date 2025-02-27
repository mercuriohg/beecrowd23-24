idade = 1
valor = 0
cont = 0
while idade > 0:
    idade = int(input())
    if idade > 0:
      cont+=1
      valor+=idade
    else:
      break
print("{:.2f}".format(valor/cont))
