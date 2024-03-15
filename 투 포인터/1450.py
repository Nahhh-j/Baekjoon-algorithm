# 냅색문제

'''
문제
세준이는 N개의 물건을 가지고 있고, 최대 C만큼의 무게를 넣을 수 있는 가방을 하나 가지고 있다.

N개의 물건을 가방에 넣는 방법의 수를 구하는 프로그램을 작성하시오.

입력
첫째 줄에 N과 C가 주어진다. N은 30보다 작거나 같은 자연수, C는 109보다 작거나 같은 음이 아닌 정수이다. 둘째 줄에 물건의 무게가 주어진다. 무게도 109보다 작거나 같은 자연수이다.

출력
첫째 줄에 가방에 넣는 방법의 수를 출력한다.
'''

import sys
input = sys.stdin.readline

n,c = map(int,input().split())
w = list(map(int,input().split()))
w1,w2 = w[:n//2],w[n//2:]
wl,wr = [],[]

def bf(arr,seq,idx,summ):
    if len(arr) == idx:
        seq.append(summ)
        return seq
    
    bf(arr,seq,idx+1,summ)
    bf(arr,seq,idx+1,summ+arr[idx])
    
    return seq

wl = bf(w1,wl,0,0)
wr = sorted(bf(w2,wr,0,0))
r = 0

for i in wl:
    if c-i < 0:
        continue
    
    start,end = 0,len(wr)
    while(start < end):
        mid = (start+end)//2
        if wr[mid] <= c-i:
            start = mid+1
        else:
            end = mid
    r+= start

print(r)