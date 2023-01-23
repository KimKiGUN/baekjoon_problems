n, r = map(int, input().split())
a = 1
b = 1
for x in range(r):
    a = a*(n-x)
    b = b*(r-x)
print(int(a/b))