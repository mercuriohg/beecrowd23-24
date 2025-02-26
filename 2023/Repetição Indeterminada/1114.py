senha = 2002
num = 0
while num != senha:
    num = int(input())
    if num == senha:
        print("Acesso Permitido")
        break
    else:
        print("Senha Invalida")
