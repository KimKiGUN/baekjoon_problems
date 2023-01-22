a, b, c = map(int, input().split())
ans = []

while a != 0:
    li = [a, b, c]
    maxs = max(li)
    mins = min(li)
    mids = (a+b+c) - (maxs + mins)
    if (maxs)**2 == (mins)**2 + (mids)**2:
        ans.append('right')
    else:
        ans.append('wrong')
    a, b, c = map(int, input().split())

for a in ans:
    print(a, end = '\n')