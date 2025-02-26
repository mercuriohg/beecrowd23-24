n = int(input())
distanc = 0
for i in range(0,n):
    tempo, velmedia = map(int,input().split())
    distanc += tempo * velmedia
print(distanc)
