cont=0
media = 0
for i in range(6):
  num = float(input())
  if num > 0:
      media += num
      cont+=1
      mediaFinal = media / cont
print("{} valores positivos".format(cont))
print("{:.1f}".format(mediaFinal))
