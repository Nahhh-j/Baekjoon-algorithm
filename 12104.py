# 순환 순열

'''
문제
두 바이너리 문자열 A와 B가 주어졌을 때, A와 XOR 했을 때, 0이 나오는 B의 순환 순열의 개수를 구하는 프로그램을 작성하시오.
순환 순열이란 순열 P = P0, P1, ..., PN-1이 있을 때, 왼쪽으로 k번 순환 이동시킨 순열이다. 즉, P를 k번 순환 이동 시키면, Pi -> Pi+k mod n 이 된다.

입력
첫째 줄에 A, 둘째 줄에 B가 주어진다. A와 B의 길이는 105를 넘지 않는 자연수이며, 두 문자열의 길이는 같다.

출력
첫째 줄에 A와 XOR했을 때, 0이 나오는 B의 순환 순열의 개수를 출력한다.
'''

import sys

A = sys.stdin.readline().strip()
B = sys.stdin.readline().strip()

def kmp_table(p):
    n = len(p)
    table = [0]*n
    j = 0
    for i in range(1,n):
        while j>0 and p[i]!=p[j]:
            j = table[j-1]
        if p[i]==p[j]:
            j+=1
            table[i]=j
    return table

def kmp_search(t,p):
    table = kmp_table(p)
    j=0
    res=0
    n=len(p)
    for i in range(len(t)-1):
        while j>0 and t[i]!=p[j]:
            j=table[j-1]
        if t[i]==p[j]:
            if j==n-1:
                if i-n+1 < n:
                    res+=1
                j=table[j]
            else:
                j+=1
    return res

T = B+B
print(kmp_search(T,A))