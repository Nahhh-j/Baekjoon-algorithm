import sys
N,M = map(int,input().split())
table = {}
length = []
for i in range(N) :
    word = sys.stdin.readline().strip()
    if len(word) < M :
        continue      
    if word in table :
        table[word] += 1
    else :
        length.append(len(word))
        table[word] = 1
 
temp = list(zip(table.items(),length))
answer = sorted(temp,key = lambda x:(-x[0][1],-x[1],x[0][0]))
for i in answer:
    print(i[0][0])