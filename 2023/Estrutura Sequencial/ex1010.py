c, nc, vc = map(float,input().split())
c2, nc2, vc2 = map(float,input().split())
pagar = (nc*vc) + (nc2*vc2)
print("VALOR A PAGAR: R$ {:.2f}".format(pagar))
