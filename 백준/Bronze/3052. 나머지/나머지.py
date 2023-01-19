su = []
for x in range(10):
    a = int(input())%42
    su.append(a)
    
new = []
for i in range(10):
    if su[i] not in new:
        new.append(su[i])
print(len(new))