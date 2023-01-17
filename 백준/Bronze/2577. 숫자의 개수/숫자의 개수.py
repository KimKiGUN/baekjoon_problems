a = int(input())
b = int(input())
c = int(input())
num = str(a*b*c)
my_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

for x in my_list:
    cnt = 0
    for i in range(len(num)):
        if num[i] == str(x):
            cnt += 1
    print(cnt)