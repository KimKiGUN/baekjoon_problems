word = input().upper()
li = []
sup = 0
ch = []
li_ch = []

for i in range(len(word)):
    if word[i] not in li:
        li.append(word[i])
        
for x in li:
    li_ch.append(word.count(x))
    
sup = max(li_ch) 

for x in li:
    if word.count(x) == sup:
        ch.append(x)
        
if len(ch) >1:
    print("?")
else:
    print(ch[0])