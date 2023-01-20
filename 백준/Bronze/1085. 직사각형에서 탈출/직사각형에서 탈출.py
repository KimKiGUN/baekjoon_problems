x, y, w, h = map(int, input().split())
di = [x, y, (w-x), (h-y)]
print(min(di))