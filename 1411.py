# 비슷한 단어

'''
문제
만약 어떤 단어A를 숌스럽게 바꿔서 또다른 단어 B로 만든다면, 그 단어는 비슷한 단어라고 한다.
어떤 단어를 숌스럽게 바꾼다는 말은 단어 A에 등장하는 모든 알파벳을 다른 알파벳으로 바꾼다는 소리다. 그리고, 단어에 등장하는 알파벳의 순서는 바뀌지 않는다. 두 개의 다른 알파벳을 하나의 알파벳으로 바꿀 수 없고, 임의의 알파벳을 자기 자신으로 바꾸는 것은 가능하다.
예를 들어, 단어 abca와 zbxz는 비슷하다. 그 이유는 a를 z로 바꾸고, b는 그대로 b, c를 x로 바꾸면, abca가 zbxz가된다.
단어가 여러 개 주어졌을 때, 몇 개의 쌍이 비슷한지 구하는 프로그램을 작성하시오.

입력
첫째 줄에 단어의 개수 N이 주어진다. 둘째 줄부터 N개의 줄에 한 줄에 하나씩 단어가 주어진다. 단어의 길이는 최대 50이고, N은 100보다 작거나 같은 자연수이다. 모든 단어의 길이는 같고, 중복되지 않는다. 또, 알파벳 소문자로만 이루어져 있다.

출력
첫째 줄에 총 몇 개의 쌍이 비슷한지 출력한다.
'''

from itertools import combinations
n = int(input())
arr=[]
res=[]
for i in range(n):
    alpha = list(input())
    t = 0
    for j in range(len(alpha)):
        x = alpha[j]
        if x in alpha:
            for k in range(len(alpha)):
                if x == alpha[k]:
                    alpha[k] = t
            t+=1
    res.append(alpha)
answer=0
a = set(map(tuple,res))
for i in a:
    num=res.count(list(i))
    if num>1:
        ar =[]
        for i in range(num):
            ar.append(i)
        c=len(list(combinations(ar,2)))
        answer += c
print(answer)