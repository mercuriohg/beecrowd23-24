num = 0
alc = 0
gas = 0
die = 0
while num != 4:
    num = int(input())
    if num == 1:
        alc+=1
    elif num == 2:
        gas+=1
    elif num == 3:
        die+=1
print("MUITO OBRIGADO")
print("Alcool: {}".format(alc))
print("Gasolina: {}".format(gas))
print("Diesel: {}".format(die))
