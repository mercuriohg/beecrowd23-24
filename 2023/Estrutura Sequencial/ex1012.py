a,b,c = map(float,input().split())
pi = 3.14159
tri = (a*c) /2 
cir = pi * (c**2)
trap = (a+b)*c / 2
qua = b**2
retang = a*b
print("TRIANGULO: {:.3f}".format(tri))
print("CIRCULO: {:.3f}".format(cir))
print("TRAPEZIO: {:.3f}".format(trap))
print("QUADRADO: {:.3f}".format(qua))
print("RETANGULO: {:.3f}".format(retang))
