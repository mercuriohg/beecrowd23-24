cod, quant = map(int,input().split())
if cod == 1:
    calc = quant*4
    print("Total: R$ {:.2f}".format(calc))
elif cod == 2:
    calc = quant*4.5
    print("Total: R$ {:.2f}".format(calc))
elif cod == 3:
    calc = quant*5
    print("Total: R$ {:.2f}".format(calc))
elif cod == 4:
    calc = quant*2
    print("Total: R$ {:.2f}".format(calc))
elif cod == 5:
    calc = quant*1.5
    print("Total: R$ {:.2f}".format(calc))
