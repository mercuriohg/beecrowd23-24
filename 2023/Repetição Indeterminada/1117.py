notas = []
while len(notas) < 2:
    nota = float(input())
    if 0 <= nota <= 10:
        notas.append(nota)
    else:
        print("nota invalida")
media = sum(notas) / len(notas)
print("media = {:.2f}".format(media))
