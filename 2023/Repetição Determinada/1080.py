maior = 0
posicao = 0
for i in range(100):
    num = int(input())
    if num > maior:
        maior = num
        posicao = i + 1
      
print(maior)
print(posicao)
