word = input()
al = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k','l','m','n'
     ,'o','p','q','r','s','t','u','v','w','x','y','z']

for x in al:
    cnt = -1
    for i in range(len(word)):
        if word[i] == x:
            cnt = i
            break
    print(cnt, end =' ')