# 격자판 채우기

'''
문제
준규는 침대에 누워서 천장을 바라보고 있었다. 천장은 격자판 모양이었고, 계속해서 천장을 바라보다 보니 이런 생각이 들었다.
세로 크기가 N이고, 가로 크기가 M인 격자판을 2x1 크기의 도미노를 이용해서 빈 공간이 없도록 채우는 방법의 수는 몇일까?
아래 그림은 N = 3, M = 6인 예이다.

N과 M이 주어졌을 때, 격자판을 2x1크기의 도미노로 채우는 방법의 수를 구하는 방법을 작성하시오. 도미노는 회전시켜 1x2크기로 채울 수 있다. 도미노로 모두 채웠을 때, 빈 칸이 존재하면 안 된다.

입력
첫째 줄에 격자판의 세로 크기 N과 가로 크기 M이 주어진다.

출력
첫째 줄에 주어진 격자판을 2x1크기의 도미노로 빈 공간이 없도록 채우는 방법의 수를 9901로 나눈 나머지를 출력한다.
'''

import sys

dp = [[-1] * (1 << 14) for _ in range(14 ** 2)]

def go(num, status):
    
    if num == n * m and status == 0:
        return 1
        
    if num >= n * m:
        return 0
        
    if dp[num][status] != -1:
        return dp[num][status]
    dp[num][status] = 0

    if status & 1:
        dp[num][status] = go(num + 1, status >> 1)
        
    else:
        dp[num][status] = go(num + 1, status >> 1 | 1 << (m - 1))
        if num % m != m - 1 and status & 2 == 0:
            dp[num][status] += go(num + 2, status >> 2)
    dp[num][status] %= 9901
    return dp[num][status]

n, m = map(int, sys.stdin.readline().split())
print(go(0, 0))