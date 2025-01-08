n = int(input())
hora = n // 3600
resto = n % 3600
minuto = resto // 60
segundo = resto%60
print("{}:{}:{}".format(hora,minuto,segundo))
