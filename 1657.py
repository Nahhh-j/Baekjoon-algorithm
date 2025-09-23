# 두부장수 장홍준

'''
문제
장홍준은 참 특이한 두부장수이다. 세로크기 N, 가로크기 M인 두부판을 가지고 2x1짜리 두부로 잘라서 판다. 그런데, 두부판의 위치마다 등급이 다르다. 그리고 2x1짜리에 등급이 어떻게 매겨지느냐에 따라 두부의 값도 천차만별이 된다. 다음 등급표를 보자.

위의 표는 2x1짜리 두부의 등급에 따라 매겨지는 두부의 가격표다. 예를 들어 “AC" 두부의 가격은 7이고, ”DB" 두부의 가격은 3이다.
세로크기 N, 가로크기 M의 두부판이 주어진다. 각 칸마다 두부의 등급이 A, B, C, D, F로 매겨져 있다. 홍준이는 전체 두부가격의 합을 최대가 되게 두부를 자르려고 한다. 2x1짜리 두부로 잘라내고 남은 한 칸짜리 두부는 가격이 0이기 때문에 버린다. 홍준이를 도와 가격이 최대가 되게 두부판을 자르는 프로그램을 작성하시오.

위 그림은 N=4, M=4 인 두부판의 한 예이다. 오른쪽 그림이 잘라낸 두부가격의 합을 최대로 한 것이다. 한 칸짜리는 쓸모없으므로 버린다.

입력
첫째 줄에는 두부판의 세로크기 N, 가로크기 M이 주어진다. N, M은 1이상 14이하의 정수이다. 그 다음 N줄에 걸쳐 M개의 문자가 주어진다. 각 문자는 그 칸의 두부의 등급을 나타내며 A, B, C, D, F 중 하나로 주어진다.

출력
첫째 줄에 잘라낸 두부가격 합의 최댓값을 출력한다.
'''

import sys
sys.setrecursionlimit(10000)

n, m = map(int, sys.stdin.readline().split())
tofu = [list(sys.stdin.readline().rstrip()) for _ in range(n)]

cost = dict().fromkeys(['A', 'B', 'C', 'D', 'F'])
for i in cost:
    cost[i] = dict().fromkeys(['A', 'B', 'C', 'D', 'F'], 0)
temp = [[10,8,7,5,1],[8,6,4,3,1],[7,4,3,2,1],[5,3,2,2,1],[1,1,1,1,0]]
for idx_i, i in enumerate(['A', 'B', 'C', 'D', 'F']):
    for idx_j, j in enumerate(['A', 'B', 'C', 'D', 'F']):
        cost[i][j] = temp[idx_i][idx_j]

dp = [[-1] * (1 << m) for _ in range(n * m)]
one_dim = [tofu[i][j] for i in range(n) for j in range(m)]

def go(num, bit):
    if num >= n * m:
        return 0
    if dp[num][bit] != -1:
        return dp[num][bit]
    dp[num][bit] = 0

    d = go(num + 1, bit >> 1)
    dp[num][bit] = max(dp[num][bit], d)

    if bit & 1 == 1:
        a = go(num + 1, bit >> 1)
        dp[num][bit] = max(dp[num][bit], a)
    else:
        if num + m < n * m and bit & 1 == 0:
            b = go(num + 1, bit >> 1 | (1 << (m - 1)))
            dp[num][bit] = max(dp[num][bit], b + cost[one_dim[num]][one_dim[num + m]])
        if num % m != (m - 1) and bit & 2 == 0:
            c = go(num + 2, bit >> 2)
            dp[num][bit] = max(dp[num][bit], c + cost[one_dim[num]][one_dim[num + 1]])
    return dp[num][bit]

print(go(0,0))