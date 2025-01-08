import math
x1,y1 = map(float,input().split())
x2,y2 = map(float,input().split())

distancia = (x2 - x1)**2 + (y2 - y1)**2
matt = math.sqrt(distancia)
print("{:.4f}".format(matt))
