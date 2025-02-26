a,b,c,d,e = map(int,input().split())
lista2 = [a,b,c,d,e]
if lista2 == sorted(lista2):
    print("C")
elif lista2 == (sorted lista2, reverse=True):
    print("D")
else:
    print("N")
