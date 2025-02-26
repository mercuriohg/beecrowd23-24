a,b = 0,1
while a != b:
    a,b = map(int,input().split())
    if a > b:
        print("Decrescente")
    elif a == b and b == a:
        break;
    else:
        print("Crescente")
