N = int(input())
temp = set({})
for i in range(N):
    a,b = input().split()
    if a == 'ChongChong' or b == 'ChongChong' :
        temp.add(a)
        temp.add(b)
        continue
    else :
        if a in temp :
            temp.add(b)
        elif b in temp :
            temp.add(a)
temp_list = list(temp)
print(len(temp_list))