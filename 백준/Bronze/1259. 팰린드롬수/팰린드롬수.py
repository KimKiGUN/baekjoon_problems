y_n = []
while True:
    try:
        pen = str(input())
        if pen == '0':
            break
        elif pen != '0':
            result = []
            for x in range(len(pen)):
                if pen[x] != pen[len(pen)-1-x]:
                    result.append('n')
                else:
                    result.append('y')
            if 'n' in result:
                y_n.append('no')
            else:
                y_n.append('yes')
    except:
        print('뭐야이거')

for x in y_n:
    print(x)