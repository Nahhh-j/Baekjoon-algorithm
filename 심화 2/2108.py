import sys
N = int(input())
temp = {}
count = 0
for i in range(N):
    a = int(sys.stdin.readline())
    count += a
    if a in temp :
        temp[a] += 1
    else :
        temp[a] = 1
        
print(round(count/N))
 
midean = list(temp.items())
midean.sort()
count = 0
for i in midean:
    count += i[1]
    if count > int(N/2) :
        print(i[0])
        break
        
mode = [key for key, value in temp.items() if value == max(temp.values())]
mode.sort()
if len(mode) > 1 :
    print(mode[1])
elif len(mode) == 1:
    print(mode[0])
    
print(max(temp.keys())-min(temp.keys()))
