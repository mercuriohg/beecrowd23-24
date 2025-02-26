band = int(input())
quebrado = 0
for i in range(band):
    lat,cop = map(int,input().split())
    if cop < lat:
        quebrado += cop
    
print(quebrado)
