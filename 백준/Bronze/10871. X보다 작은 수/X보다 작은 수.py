n, x = map(int, input().split())
num = list(map(int, input().split()))

for su in num:
    if su < x:
        print(su, end = ' ')