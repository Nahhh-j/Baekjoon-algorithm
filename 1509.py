# 팰린드롬 분할

'''
문제
세준이는 어떤 문자열을 팰린드롬으로 분할하려고 한다. 예를 들어, ABACABA를 팰린드롬으로 분할하면, {A, B, A, C, A, B, A}, {A, BACAB, A}, {ABA, C, ABA}, {ABACABA}등이 있다.
분할의 개수의 최솟값을 출력하는 프로그램을 작성하시오.

입력
첫째 줄에 문자열이 주어진다. 이 문자열은 알파벳 대문자로만 이루어져 있고, 최대 길이는 2,500이다.

출력
첫째 줄에 팰린드롬 분할의 개수의 최솟값을 출력한다.
'''

import sys
sys.setrecursionlimit(10**8)
input = sys.stdin.readline


def palindrome():
    for i in range(L):
        is_p[i][i] = 1
    
    for i in range(1,L):
        if string[i-1] == string[i]:
            is_p[i-1][i] = 1
    
    for l in range(3, L+1):
        for start in range(L-l+1):
            end = start + l -1
            if string[start] == string[end] and is_p[start+1][end-1]:
                is_p[start][end] = 1
    
    for end in range(L):
        for start in range(end+1):
            if is_p[start][end]:
                dp[end] = min(dp[end], dp[start-1] + 1)
            else:
                dp[end] = min(dp[end], dp[end-1] + 1)

if __name__ == "__main__":
    string = input().strip()
    L = len(string)
    dp = [2500 for _ in range(L+1)]
    dp[-1] = 0
    is_p = [[0 for _ in range(L)] for _ in range(L)]
    
    palindrome()
    print(dp[L-1])