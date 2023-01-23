n = int(input())
arr = [list(map(int, input().split())) for i in range(n)]

for c in arr:
    r = 0
    li = []
    for w in range(c[1]):
        ws = 101 + w
        for h in range(c[0]):
            r = ws + 100*h
            li.append(r)
    
    print(li[c[2]-1])