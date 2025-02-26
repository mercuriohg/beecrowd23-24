n = int(input())
out = 0
i = 0
for g in range(n):
    num = int(input())
    if num >= 10 and num <= 20:
        i += 1
    else:
        out+=1
    
print("{} in".format(i))
print("{} out".format(out))
